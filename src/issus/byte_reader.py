class OutOfBounds(Exception):
    pass


def read_little_endian(data, offset, size):

    if offset + size > len(data):
        raise OutOfBounds(f"the field: {offset + size} > data: {data}")

    field_bytes = data[offset : offset + size]

    value = int.from_bytes(field_bytes, byteorder="little")

    return value
