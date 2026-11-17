from issus.byte_reader import read_little_endian


def test_two_size_byte():
    data = bytes.fromhex("e803")
    integer_value = read_little_endian(data, 0, 2)
    assert integer_value == 1000


def test_offset():
    data = bytes.fromhex("e85674aa")
    integer_value = read_little_endian(data, 1, 3)
    assert integer_value == 11170902


def test_four_size_byte():
    data = bytes.fromhex("e85674aa")
    integer_value = read_little_endian(data, 0, 4)
    assert integer_value == 2859751144
