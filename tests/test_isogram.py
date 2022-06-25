from scripts.isogram import isogram


def test_isogram_returns_true():
    assert isogram("word") == True


def test_isogram_returns_false():
    assert isogram("ii") == False


def test_isogram_returns_false_2():
    assert isogram("iii") == False


def test_isogram_returns_true_3():
    assert isogram("i-j-o q") == True


def test_isogram_returns_true_lumberjacks():
    assert isogram("lumberjacks") == True


def test_isogram_returns_true_background():
    assert isogram("background") == True


def test_isogram_returns_true_downstream():
    assert isogram("downstream") == True


def test_isogram_returns_true_sixyearold():
    assert isogram("six-year-old") == True


def test_eleven_returns_false():
    assert isogram("eleven") == False


def test_Alphabet_returns_false():
    assert isogram("Alphabet") == False


def test_Alphabet_returns_false():
    assert isogram("alphAbet") == False
