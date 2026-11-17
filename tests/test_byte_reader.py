import pytest

from issus.byte_reader import OutOfBounds, read_little_endian


def test_two_size_byte():
    data = bytes.fromhex("e8 03")
    integer_value = read_little_endian(data, 0, 2)
    assert integer_value == 1000


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
    with pytest.raises(OutOfBounds):
        data = bytes.fromhex("a4 90 39 45")
        read_little_endian(data, 0, 6)
