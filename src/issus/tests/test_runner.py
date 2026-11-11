from issus.runner import list_fixture_path


def test_create_temp_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "94diir4.fix"
    t = d / "8485hf4.fix"
    p.touch()
    t.touch()
    prefix = "94d"

    result = list_fixture_path(d, prefix)

    assert result == [p]
