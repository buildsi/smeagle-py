from typing import Dict

import elftools
from cle.backends.elf import ELF as ElfBase
from elftools.common.exceptions import ELFError
from elftools.dwarf.descriptions import set_global_machine_arch
from elftools.dwarf.dwarfinfo import DWARFInfo
from elftools.dwarf.locationlists import LocationParser

from smeagle.logger import logger

from .. import register_backend
from .corpus import ElfCorpus
from .variable_type import VariableType


class ELF(ElfBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Post processing steps
        self.corpus = {}
        self.load_corpus()

    def load_corpus(self):
        """
        Check for dwarf info, and if found, load the corpus from it.
        """
        if self.has_dwarf_info:
            # load DWARF information
            try:
                dwarf = self._reader.get_dwarf_info()
            except ELFError:
                logger.warning(
                    "An exception occurred in pyelftools when loading the DWARF information for %s. "
                    "Marking DWARF as not available for this binary.",
                    self.binary_basename,
                    exc_info=True,
                )
                self.has_dwarf_info = False
                return

        # Prepare exported symbols
        dynamic_symbols = self._load_dynamic_symbols()

        # Prepare a corpus to populate
        self.corpus = ElfCorpus(self.binary, arch=self.arch, symbols=dynamic_symbols)

        # Load corpus. This is redundant for some of _load_dies
        self._load_corpus(dwarf)
        self.corpus.add_locations()

    def _prepare_location_parser(self, dwarf):
        """
        Prepare the location parser using the dwarf info
        """
        location_lists = dwarf.location_lists()

        # Needed to decode register names in DWARF expressions.
        set_global_machine_arch(self._reader.get_machine_arch())
        self.loc_parser = LocationParser(location_lists)

    def _load_dynamic_symbols(self):
        """
        We only care about dynamic symbols
        """
        dynamic_symbols = {}
        for section in self._reader.iter_sections():
            if section.name == ".dynsym":
                for symbol in section.iter_symbols():
                    if (
                        symbol.entry["st_info"]["bind"] != "STB_GLOBAL"
                        or symbol.entry["st_info"]["type"] == "STT_DELETED"
                    ):
                        continue
                    # undefined is import, and everything else is export
                    direction = "export"
                    if symbol.entry["st_shndx"] == "SHN_UNDEF":
                        direction = "import"
                    dynamic_symbols[symbol.name] = direction
        return dynamic_symbols

    def _load_corpus(self, dwarf: DWARFInfo):
        """
        Load DIEs and CUs from DWARF into corpus

        :param dwarf:   The DWARF info object from pyelftools.
        :return:        None
        """
        # DW_TAG_base_types, and DW_TAG_typedef
        type_list: Dict[int, VariableType] = {}
        type_die_lookup: Dict[int, elftools.dwarf.die.DIE] = {}

        # The corpus needs the location parser to get registers
        self._prepare_location_parser(dwarf)
        self.corpus.loc_parser = self.loc_parser

        # Parse all dies recursively
        def parse_die_types(die):
            type_die_lookup[die.offset] = die
            for child in die.iter_children():
                parse_die_types(child)

        for cu in dwarf.iter_CUs():
            # scan the whole die tree for DW_TAG_base_type
            try:
                for die in cu.iter_DIEs():
                    if die.tag == "DW_TAG_base_type":
                        var_type = VariableType.read_from_die(die)
                        if var_type is not None:
                            type_list[die.offset] = var_type
                    parse_die_types(die)
            except KeyError:
                # pyelftools is not very resilient - we need to catch KeyErrors here
                continue

            # Provide type information to the corpus
            self.corpus.type_die_lookup = type_die_lookup

            top_die = cu.get_top_DIE()
            if top_die.tag != "DW_TAG_compile_unit":
                logger.warning("ignore a top die with unexpected tag")
                continue

            # First round is going to generate all base types, etc.
            for die_child in cu.iter_DIE_children(top_die):
                self.corpus.add_dwarf_information_entry(die_child)


register_backend("elf", ELF)
