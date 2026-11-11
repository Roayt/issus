import argparse
import sys
from collections import Counter

from issus.runner import compare_fixtures, count_err_codes

fields = "err_code", "rodata_hash", "text_cnt", "text_off", "entry_pc", "calldests_hash"


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("folder")
    run_parser.add_argument("--only", default="")
    run_parser.add_argument("--show-fails", type=int, default=0)
    run_parser.add_argument("--min-pass", type=int, default=0)

    args = parser.parse_args()

    err_code_counts = count_err_codes(args.folder, args.only)
    outcome_counts, failures = compare_fixtures(args.folder, args.only)

    total = err_code_counts.total()
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
