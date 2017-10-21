"""Test function for summy module."""

import pytest

TEST_DATA = [("1 2 3", 6), ("1 2 3 4", 10), ("1 2 3 4 5", 15),
             ("10 10", 20), ("0 0", 0), ("150 150 300", 600),
             ("900 900", 1800), ("-1 5 -10 10", 4), ("-20 7", -13)]


@pytest.mark.parametrize('string, result', TEST_DATA)
def test_summy(string, result):
    """Test for summy function."""
    from summy import summy
    assert summy(string) == result
