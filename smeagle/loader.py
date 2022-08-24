from cle.backends import Backend
from cle.loader import Loader
from cle.utils import stream_or_path

from smeagle.backends import ALL_BACKENDS


class Loader(Loader):
    """
    Wrapper around the cle.Loader to add a corpus and custom backend
    """

    def __init__(self, *args, **kwargs):
        kwargs["load_debug_info"] = False
        kwargs["auto_load_libs"] = False
        super().__init__(*args, **kwargs)

    @property
    def corpus(self):
        if hasattr(self.main_object, "corpus"):
            return self.main_object.corpus
        raise ValueError("No corpus available.")

    def _static_backend(self, spec, ignore_hints=False):
        if not ignore_hints:
            for ident in self._possible_idents(spec):
                try:
                    return self._backend_resolver(self._lib_opts[ident]["backend"])
                except KeyError:
                    pass

        with stream_or_path(spec) as stream:
            for rear in ALL_BACKENDS.values():
                if rear.is_default and rear.is_compatible(stream):
                    return rear

    @staticmethod
    def _backend_resolver(backend, default=None):
        if isinstance(backend, type) and issubclass(backend, Backend):
            return backend
        elif backend in ALL_BACKENDS:
            return ALL_BACKENDS[backend]
        elif backend is None:
            return default
        else:
            raise ValueError("Invalid backend: %s" % backend)
