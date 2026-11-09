import argparse

from issus.runner import compare_fixtures, count_err_codes


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("folder")
    run_parser.add_argument("--only", default="")

    args = parser.parse_args()

    err_code_counts = count_err_codes(args.folder, args.only)
    outcome_counts, failure = compare_fixtures(args.folder, args.only)

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

    for name, expected, actual in failure:
        print(
            f"failed file: {name}\n"
            f"expected output: {expected}\n"
            f"actual outcome: {actual}"
        )
