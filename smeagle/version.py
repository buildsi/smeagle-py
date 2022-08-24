__version__ = "0.0.12"
AUTHOR = "Vanessa Sochat"
EMAIL = "vsoch@users.noreply.github.com"
NAME = "smeagle"
PACKAGE_URL = "https://github.com/buildsi/smeagle-py"
KEYWORDS = "ELF, DWARF, binary metadata"
DESCRIPTION = "Fact generation for elf binaries with debug"
LICENSE = "LICENSE"

################################################################################
# Global requirements

# Since we assume wanting Singularity and lmod, we require spython and Jinja2

INSTALL_REQUIRES = (
    ("cle", {"min_version": None}),
    ("pyelftools", {"min_version": None}),
)

TESTS_REQUIRES = (("pytest", {"min_version": "4.6.2"}),)

################################################################################
# Submodule Requirements (versions that include database)

INSTALL_REQUIRES_ALL = INSTALL_REQUIRES + TESTS_REQUIRES
