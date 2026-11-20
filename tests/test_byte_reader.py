import pytest

from issus.byte_reader import read_little_endian
from issus.elf_parser_error import OutOfBounds


def test_one_size_byte():
    data = bytes.fromhex("e8")
    integer_value = read_little_endian(data, 0, 1)
    assert integer_value == 232


def test_two_size_byte():
    data = bytes.fromhex("e8 03")
    integer_value = read_little_endian(data, 0, 2)
    assert integer_value == 1000


def test_read_eight_size_byte():
    data = bytes.fromhex("e8 03 86 00 00 00 70 00")
    integer_value = read_little_endian(data, 0, 8)
    assert integer_value == 31525197400376296


def test_offset():
    data = bytes.fromhex("e8 56 74 aa")
    integer_value = read_little_endian(data, 1, 3)
    assert integer_value == 11170902


def test_four_size_byte():
    data = bytes.fromhex("e8 56 74 aa")
    integer_value = read_little_endian(data, 0, 4)
    assert integer_value == 2859751144


def test_read_data_before_end():
    data = bytes.fromhex("a4 90 39 45")
    integer_value = read_little_endian(data, 0, 2)
    assert integer_value == 37028


def test_outofbound():
    data = bytes.fromhex("a4 90 39 45")
    with pytest.raises(OutOfBounds):
        read_little_endian(data, 0, 5)
