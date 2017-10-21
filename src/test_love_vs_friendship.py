"""Test functions for love_vs_friendship module."""

import pytest

TEST_DATA = [('attitude', 100), ('friends', 75), ('family', 66),
             ('selfness', 99), ('knowledge', 96), ('serenity', 115),
             ('supercalifragilisticexpialidocious', 379),
             ('dog', 26), ('cat', 24)]


@pytest.mark.parametrize('string, result', TEST_DATA)
def test_words_to_marks(string, result):
    """Test words_to_marks function."""
    from love_vs_friendship import words_to_marks
    assert words_to_marks(string) == result
