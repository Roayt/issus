from issus.byte_reader import read_little_endian


def parse_program_elf_value(elf_value, value):

    p_type = read_little_endian(elf_value, value, 4)
    p_flags = read_little_endian(elf_value, value, 4)
    p_offset = read_little_endian(elf_value, value, 8)
    p_vaddar = read_little_endian(elf_value, value, 8)
    p_paddar = read_little_endian(elf_value, value, 8)
    p_filesz = read_little_endian(elf_value, value, 8)
    p_memsz = read_little_endian(elf_value, value, 8)
    p_align = read_little_endian(elf_value, value, 8)

    return (p_type, p_flags, p_offset, p_vaddar, p_paddar, p_filesz, p_memsz, p_align)
