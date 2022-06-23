from scripts.isogram import isogram


def test_isogram_returns_true():
    assert isogram("word") == True


def test_isogram_returns_false():
    assert isogram("ii") == False
