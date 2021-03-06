"""Test function for selective_array_reversing function."""

import pytest

TEST_DATA = [([2, 4, 6, 8, 10, 12, 14, 16], 3, [6, 4, 2, 12, 10, 8, 16, 14]),
             ([2, 4, 6, 8, 10, 12, 14, 16], 2, [4, 2, 8, 6, 12, 10, 16, 14]),
             ([1, 2, 3, 4, 5, 6], 2, [2, 1, 4, 3, 6, 5]),
             ([1, 2, 3, 4, 5, 6], 0, [1, 2, 3, 4, 5, 6]),
             ([1, 2, 3, 4, 5, 6], 10, [6, 5, 4, 3, 2, 1]),
             ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34,
              36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66,
              68, 70, 72, 74, 76, 78, 80, 82, 84, 86], 36, [72, 70, 68, 66,
              64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34,
              32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 86,
              84, 82, 80, 78, 76, 74]),
             ([3, 6, 9, 12, 15, 18], 45, [18, 15, 12, 9, 6, 3]),
             ([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
              85, 90, 95, 100, 105, 110, 115, 120, 125, 130],
              26, [130, 125, 120, 115, 110, 105, 100, 95, 90, 85, 80, 75, 70,
              65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]),
             ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
              19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
              35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45],
              3, [3, 2, 1, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13, 18, 17,
              16, 21, 20, 19, 24, 23, 22, 27, 26, 25, 30, 29, 28, 33, 32, 31,
              36, 35, 34, 39, 38, 37, 42, 41, 40, 45, 44, 43])]


@pytest.mark.parametrize("arr, l, result", TEST_DATA)
def test_sel_reverse(arr, l, result):
    """Test for sel_reverse function."""
    from selective_array_reversing import sel_reverse
    assert sel_reverse(arr, l) == result
