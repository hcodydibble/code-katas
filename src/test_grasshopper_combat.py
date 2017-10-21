"""Test function for sum_of_lowest_int module."""

import pytest

TEST_DATA = [(100, 5, 95), (83, 16, 67), (20, 30, 0),
             (100, 101, 0), (10, 3, 7), (25, 5, 20), (100, 98, 2),
             (1, 2, 0)]


@pytest.mark.parametrize("h, d, result", TEST_DATA)
def test_combat(h, d, result):
    """Test for combat function."""
    from grasshopper_combat import combat
    assert combat(h, d) == result
