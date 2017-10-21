"""Test function for sum_of_lowest_int module."""

import pytest

TEST_DATA = [([5, 8, 12, 18, 22], 13), ([7, 15, 12, 18, 22], 19),
             ([25, 42, 12, 18, 22], 30), ([234, 5235, 2349812, 428], 662),
             ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 3), ([3, 7], 10),
             ([132, 532, 13892], 664)]


@pytest.mark.parametrize("numbers, result", TEST_DATA)
def test_sum_two_smallest_numbers(numbers, result):
    """Test for sum_two_smallest_numbers function."""
    from sum_of_lowest_int import sum_two_smallest_numbers
    assert sum_two_smallest_numbers(numbers) == result
