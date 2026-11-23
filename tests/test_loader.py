import pytest

from issus.loader import load


def test_loader_out_of_bound_error():
    features = set()
    deploy_check = False
    data = bytes.fromhex(
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    )
    result = load(data, features, deploy_check)

    assert result == (21, 0, 0, 0, 0, 0)


def test_version_4_return_22():
    features = set()
    deploy_check = False
    data = bytes.fromhex(
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 04 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    )
    result = load(data, features, deploy_check)

    assert result == (22, 0, 0, 0, 0, 0)


def test_version_7_return_22():
    features = set()
    deploy_check = False
    data = bytes.fromhex(
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 07 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    )
    result = load(data, features, deploy_check)

    assert result == (22, 0, 0, 0, 0, 0)


def test_0x01000000_trap_return_22():
    features = set()
    deploy_check = False
    data = bytes.fromhex(
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00"
    )
    result = load(data, features, deploy_check)

    assert result == (22, 0, 0, 0, 0, 0)


def test_version_3_not_implemented():
    features = set()
    deploy_check = False
    data = bytes.fromhex(
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
    )

    with pytest.raises(NotImplementedError):
        load(data, features, deploy_check)