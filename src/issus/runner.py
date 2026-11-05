from collections import Counter
from pathlib import Path

from issus.fixture import parse_fixture


def count_err_codes(fixture_dir):
    fixture_paths = sorted(Path(fixture_dir).glob("*.fix"))
    error_code_list=[]

    for fixture_path in sorted(fixture_paths):
        fixture=parse_fixture(fixture_path)
        error_code=fixture.output.err_code

        error_code_list.append(error_code)

    err_code_counts=Counter(error_code_list)

    return err_code_counts


if __name__=="__main__":
    err_code_counts=count_err_codes(Path.home()/'issus-data'/'test-vectors'/'elf_loader'/'fixtures')
    total=err_code_counts.total()
    print(f"Total no of file:{total}")
    rows=sorted(err_code_counts.items())


    for err_code,count in rows:
        print(f"err_code: {err_code}: {count}")
    