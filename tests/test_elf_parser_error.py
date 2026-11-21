from issus.elf_parser_error import (
    InvalidProgramHeader,
    OutOfBounds,
    SectionNotInOrder,
    to_elf_error,
)


def test_out_of_bounds():
    out_of_bounds = OutOfBounds()
    error_code = to_elf_error(out_of_bounds)
    assert error_code == 21


def test_invalid_program_header():
    invalid_program_header = InvalidProgramHeader()
    error_code = to_elf_error(invalid_program_header)
    assert error_code == 23


def test_section_not_in_order():
    section_not_in_order = SectionNotInOrder()
    error_code = to_elf_error(section_not_in_order)

    assert error_code == 1
