import pytest

from issus.elf_header import parse_elf_value
from issus.elf_parser_error import OutOfBounds


def test_header_bytes():
    data = bytes.fromhex(
        "7f 45 4c 46 01 02 03 04 05 00 00 00 00 00 00 00 0600 07 00 08 00 00 00 09 00 00 00 00 00 00 00 0a 00 00 00 00 00 00 00 0b 00 00 00 00 00 00 00 0c 00 00 00 0d 00 0e 00 0f 00 10 00 11 00 12 00"
    )
    result = parse_elf_value(data)

    assert result == (
        b"\x7fELF",
        1,
        2,
        3,
        4,
        5,
        b"\x00\x00\x00\x00\x00\x00\x00",
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
    )


def test_outofbound():
    data = bytes.fromhex(
        "7f 45 4c 46 01 02 03 04 05 00 00 00 00 00 00 00 0600 07 00 08 00 00 00 09 00 00 00 00 00 00 00 0a 00 00 00 00 00 00 00 0b 00 00 00 00 00 00 00 0c 00 00 00 0d 00 0e 00 0f 00 10 00 11 00 12 "
    )
    with pytest.raises(OutOfBounds):
        parse_elf_value(data)
