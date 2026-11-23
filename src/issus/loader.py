from issus.byte_reader import read_little_endian
from issus.elf_error import ElfError
from issus.elf_parser_error import ElfParserError, to_elf_error


def load(elf_bytes, feature_numbers, deploy_check):

    try:
        e_flags = read_little_endian(elf_bytes, 48, 4)

    except ElfParserError as error:
        code = to_elf_error(error)
        return code, 0, 0, 0, 0, 0

    if e_flags <= 3:
        raise NotImplementedError
    else:
        return ElfError.UnsupportedSBPFVersion, 0, 0, 0, 0, 0
