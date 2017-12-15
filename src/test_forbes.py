"""Test function for forbes module."""


def test_forbes_returns_correct_names():
    from forbes import richie_rich
    answer = richie_rich()
    assert 'Mark Zuckerberg' in answer
    assert 'Phil Knight' in answer
    assert 78 and 32 in answer
