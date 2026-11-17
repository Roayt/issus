def read_little_endian(data, offset, size):

    field_bytes = data[offset : offset + size]

    value = int.from_bytes(field_bytes, byteorder="little")

    return value
