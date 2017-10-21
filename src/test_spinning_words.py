"""Test function for spinning_words module."""

import pytest

TEST_DATA = [("Welcome", "emocleW"),
             ("Some of these will be reversed",
              "Some of eseht will be desrever"),
             ("One of these will be", "One of eseht will be"),
             ("Beer and code", "Beer and code"),
             ("Cats rule and dogs drool", "Cats rule and dogs loord")]


@pytest.mark.parametrize('string, result', TEST_DATA)
def test_spin_words(string, result):
    """Test for spin_words function."""
    from spinning_words import spin_words
    assert spin_words(string) == result
