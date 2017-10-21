"""Test function for who_at_the_cookie module."""

import pytest

TEST_DATA = [("Ryan", "Who ate the last cookie? It was Zach!"),
             (2.3, "Who ate the last cookie? It was Monica!"),
             (26, "Who ate the last cookie? It was Monica!"),
             (True, "Who ate the last cookie? It was the dog!"),
             (False, "Who ate the last cookie? It was the dog!"),
             ("STRING IT UP BRUH", "Who ate the last cookie? It was Zach!"),
             (19284, "Who ate the last cookie? It was Monica!"),
             (".", "Who ate the last cookie? It was Zach!")]


@pytest.mark.parametrize('x, result', TEST_DATA)
def test_cookie(x, result):
    """Test for cookie function."""
    from who_ate_the_cookie import cookie
    assert cookie(x) == result
