import argparse
import sys
from collections import Counter
from pathlib import Path

from issus.elf_header import parse_elf_value, take_elf_data
from issus.fixture import parse_fixture
from issus.runner import compare_fixtures, count_err_codes

fields = "err_code", "rodata_hash", "text_cnt", "text_off", "entry_pc", "calldests_hash"


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    run_parser = subparsers.add_parser("run")
    inspect_parser = subparsers.add_parser("inspect")
    inspect_parser.add_argument("file")
    run_parser.add_argument("folder")
    run_parser.add_argument("--only", default="")
    run_parser.add_argument("--show-fails", type=int, default=0)
    run_parser.add_argument("--min-pass", type=int, default=0)

    args = parser.parse_args()

    if args.command == "inspect":
        path = Path(args.file)
        parsed_fixture = parse_fixture(path)
        elf_bytes = take_elf_data(parsed_fixture)

        (
            ei_mag,
            ei_class,
            ei_data,
            ei_version,
            ei_osabi,
            ei_abiversion,
            ei_pad,
            e_type,
            e_machine,
            e_version,
            e_entry,
            e_phoff,
            e_shoff,
            e_flags,
            e_ehsize,
            e_phentsize,
            e_phnum,
            e_shentsize,
            e_shnum,
            e_shstrndx,
        ) = parse_elf_value(elf_bytes)
        print(
            f"ei_mag:{ei_mag}\n"
            f"ei_class:{ei_class}\n"
            f"ei_data:{ei_data}\n"
            f"ei_version:{ei_version}\n"
            f"ei_osabi:{ei_osabi}\n"
            f"ei_abiversion:{ei_abiversion}\n"
            f"ei_pad:{ei_pad}\n"
            f"e_type:{e_type}\n"
            f"e_machine:{e_machine}\n"
            f"e_version:{e_version}\n"
            f"e_entry:{e_entry}\n"
            f"e_phoff:{e_phoff}\n"
            f"e_shoff:{e_shoff}\n"
            f"e_flags:{e_flags}\n"
            f"e_ehsize:{e_ehsize}\n"
            f"e_phentsize:{e_phentsize}\n"
            f"e_phnum:{e_phnum}\n"
            f"e_shentsize:{e_shentsize}\n"
            f"e_shnum:{e_shnum}\n"
            f"e_shstrndx:{e_shstrndx}\n"
        )

    else:
        err_code_counts = count_err_codes(args.folder, args.only)
        outcome_counts, failures = compare_fixtures(args.folder, args.only)

        total = err_code_counts.total()
        if total == 0:
            sys.exit("The folder path or a prefix doesn't match any .fix file")
        print(f"Total no of file:{total}")
        rows = sorted(err_code_counts.items())

        for err_code, count in rows:
            print(f"err_code: {err_code}: {count}")

        total = outcome_counts.total()

        print(
            f"Total:{total}\n"
            f"Passed:{outcome_counts['passed']}\n"
            f"Failed:{outcome_counts['failed']}\n"
            f"Not Implemented:{outcome_counts['not implemented']}"
        )

        for file_name, expected, actual in failures[: args.show_fails]:
            print(f"failed file: {file_name}\n")

            for field, expc, act in zip(fields, expected, actual):
                print(f"{field}: expected: {expc}: actual: {act}")

        pairs = []
        for file_name, expected, actual in failures:
            pair = expected[0], actual[0]
            pairs.append(pair)
        pair_counts = Counter(pairs)

        for pair, count in sorted(pair_counts.items()):
            expected_output, actual_output = pair
            print(f"expected: {expected_output}, actual: {actual_output}: {count}")

        if outcome_counts["passed"] < args.min_pass:
            sys.exit(1)
