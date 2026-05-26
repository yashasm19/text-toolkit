from toolkit.utils import word_count, reverse_words, is_palindrome, truncate


def test_word_count():
    result = word_count("hello world hello")
    assert result["hello"] == 2
    assert result["world"] == 1


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False


def test_truncate():
    assert truncate("hello world", 8) == "hello..."
    assert truncate("hi", 10) == "hi"
