from collections import Counter
from pathlib import Path

from issus.fixture import parse_fixture
from issus.loader import load


def count_err_codes(fixture_dir):
    fixture_paths = sorted(Path(fixture_dir).glob("*.fix"))
    error_code_list = []

    for fixture_path in sorted(fixture_paths):
        fixture = parse_fixture(fixture_path)
        error_code = fixture.output.err_code

        error_code_list.append(error_code)

    err_code_counts = Counter(error_code_list)

    return err_code_counts


err_code_counts = count_err_codes(
    Path.home() / "issus-data" / "test-vectors" / "elf_loader" / "fixtures"
)
total = err_code_counts.total()
print(f"Total no of file:{total}")
rows = sorted(err_code_counts.items())


for err_code, count in rows:
    print(f"err_code: {err_code}: {count}")


def compare_fixtures(fixture_dir):
    fixture_paths = sorted(Path(fixture_dir).glob("*.fix"))
    outcomes = []
    for fixture_path in fixture_paths:
        parsed_fixture = parse_fixture(fixture_path)
        elf_data = parsed_fixture.input.elf_data
        features = parsed_fixture.input.features.features
        deploy_checks = parsed_fixture.input.deploy_checks

        try:
            actual = load(elf_data, features, deploy_checks)
        except NotImplementedError:
            outcomes.append("not implemented")

        else:
            expected = (
                parsed_fixture.output.err_code,
                parsed_fixture.output.rodata_hash,
                parsed_fixture.output.text_cnt,
                parsed_fixture.output.text_off,
                parsed_fixture.output.entry_pc,
                parsed_fixture.output.calldests_hash,
            )

            outcomes.append("passed" if expected == actual else "failed")

    outcome_counts = Counter(outcomes)

    return outcome_counts


if __name__ == "__main__":
    outcome_counts = compare_fixtures(
        Path.home() / "issus-data" / "test-vectors" / "elf_loader" / "fixtures"
    )
    total = outcome_counts.total()

    print(
        f"Total:{total}\n"
        f"Passed:{outcome_counts['passed']}\n"
        f"Failed:{outcome_counts['failed']}\n"
        f"Not Implemented:{outcome_counts['not implemented']}"
    )
