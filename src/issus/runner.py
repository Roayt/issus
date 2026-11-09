from collections import Counter
from pathlib import Path

from issus.fixture import parse_fixture
from issus.loader import load


def list_fixture_path(folder, prefix):
    all_paths = Path(folder).glob("*.fix")

    matching_paths = []
    for path in all_paths:
        name = path.name
        match = name.startswith(prefix)
        if match:
            matching_paths.append(path)

    return sorted(matching_paths)


def count_err_codes(folder, prefix):

    fixture_paths = list_fixture_path(folder, prefix)

    error_code_list = []

    for fixture_path in fixture_paths:
        fixture = parse_fixture(fixture_path)
        error_code = fixture.output.err_code

        error_code_list.append(error_code)

    err_code_counts = Counter(error_code_list)

    return err_code_counts


def compare_fixtures(folder, prefix):
    fixture_paths = list_fixture_path(folder, prefix)
    outcomes = []
    failures = []
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

            if actual != expected:
                filename = fixture_path.name
                expected_outcome = expected
                actual_value = actual

                failure_object = filename, expected_outcome, actual_value
                failures.append(failure_object)
                outcomes.append("failed")
            else:
                outcomes.append("passed")

    outcome_counts = Counter(outcomes)

    return outcome_counts, failures
