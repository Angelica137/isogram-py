from scripts.isogram import isogram


def test_isogram_returns_true():
    assert isogram("word") == True
