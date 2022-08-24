ALL_BACKENDS = {}


def register_backend(name, cls):
    ALL_BACKENDS.update({name: cls})


from .elf import ELF
