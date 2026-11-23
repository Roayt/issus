from issus.elf_error import ElfError


class ElfParserError(Exception):
    pass


class InvalidFileHeader(ElfParserError):
    pass


class InvalidProgramHeader(ElfParserError):
    pass


class InvalidSectionHeader(ElfParserError):
    pass


class InvalidString(ElfParserError):
    pass


class StringTooLong(ElfParserError):
    pass


class OutOfBounds(ElfParserError):
    pass


class InvalidSize(ElfParserError):
    pass


class Overlap(ElfParserError):
    pass


class SectionNotInOrder(ElfParserError):
    pass


class NoSectionNameStringTable(ElfParserError):
    pass


class InvalidDynamicSectionTable(ElfParserError):
    pass


class InvalidRelocationTable(ElfParserError):
    pass


class InvalidAlignment(ElfParserError):
    pass


class NoStringTable(ElfParserError):
    pass


class NoDynamicStringTable(ElfParserError):
    pass


def to_elf_error(error):

    if isinstance(error, OutOfBounds):
        return ElfError.ValueOutOfBounds

    if isinstance(error, InvalidProgramHeader):
        return ElfError.InvalidProgramHeader
    else:
        return ElfError.FailedToParse
