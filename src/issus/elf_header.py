from issus.byte_reader import read_little_endian


def take_elf_data(fixture):
    elf_data_value = fixture.input.elf_data

    return elf_data_value


def parse_elf_value(elf_value):

    ei_mag = elf_value[0:4]
    ei_class = read_little_endian(elf_value, 4, 1)
    ei_data = read_little_endian(elf_value, 5, 1)
    ei_version = read_little_endian(elf_value, 6, 1)
    ei_osabi = read_little_endian(elf_value, 7, 1)
    ei_abiversion = read_little_endian(elf_value, 8, 1)
    ei_pad = elf_value[9:16]
    e_type = read_little_endian(elf_value, 16, 2)
    e_machine = read_little_endian(elf_value, 18, 2)
    e_version = read_little_endian(elf_value, 20, 4)
    e_entry = read_little_endian(elf_value, 24, 8)
    e_phoff = read_little_endian(elf_value, 32, 8)
    e_shoff = read_little_endian(elf_value, 40, 8)
    e_flags = read_little_endian(elf_value, 48, 4)
    e_ehsize = read_little_endian(elf_value, 52, 2)
    e_phentsize = read_little_endian(elf_value, 54, 2)
    e_phnum = read_little_endian(elf_value, 56, 2)
    e_shentsize = read_little_endian(elf_value, 58, 2)
    e_shnum = read_little_endian(elf_value, 60, 2)
    e_shstrndx = read_little_endian(elf_value, 62, 2)

    return (
        ei_mag,
        ei_class,
        ei_data,
        ei_version,
        ei_osabi,
        ei_abiversion,
        ei_pad,
        e_type,
        e_machine,
        e_version,
        e_entry,
        e_phoff,
        e_shoff,
        e_flags,
        e_ehsize,
        e_phentsize,
        e_phnum,
        e_shentsize,
        e_shnum,
        e_shstrndx,
    )
