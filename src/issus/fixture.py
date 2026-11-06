from pathlib import Path

import elf_pb2

fixture_file = (
    Path.home()
    / "issus-data"
    / "test-vectors"
    / "elf_loader"
    / "fixtures"
    / "0019720d5a01824c2169fa7d7e41d7ee16b6795c_600628.fix"
)


def parse_fixture(path):
    elf_parser = elf_pb2.ELFLoaderFixture()
    fixture_bytes = path.read_bytes()

    elf_parser.ParseFromString(
        fixture_bytes,
    )

    return elf_parser


if __name__ == "__main__":
    data = parse_fixture(fixture_file)

    print(
        f"error code: {data.output.err_code}\n"
        f"rodata hash: {hex(data.output.rodata_hash)}\n"
        f"calldests hash: {hex(data.output.calldests_hash)}\n"
        f"entry pc: {data.output.entry_pc}\n"
        f"text off: {data.output.text_off}\n"
        f"text cnt: {data.output.text_cnt}\n"
        f"number of features: {len(data.input.features.features)}\n"
        f"deploy check: {data.input.deploy_checks}"
    )
