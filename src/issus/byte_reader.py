def byte_reader(raw_byte, off_set, size):

    t = raw_byte[off_set : off_set + size]

    calculated_decimal = int.from_bytes(t, byteorder="little")

    return calculated_decimal
