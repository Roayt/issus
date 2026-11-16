from issus.byte_reader import byte_reader


def test_byte():
    byte = bytes.fromhex("e803")
    t = byte_reader(byte, 0, 2)
    assert t == 1000


def test_offset():
    byte = bytes.fromhex("e85674aa")
    t = byte_reader(byte, 1, 3)
    assert t == 11170902
