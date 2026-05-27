from toolkit.utils import (
    word_count, reverse_words, is_palindrome,
    truncate, capitalize_words, count_vowels,
    remove_duplicates, slug
)


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


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"


def test_count_vowels():
    assert count_vowels("hello world") == 3
    assert count_vowels("rhythm") == 0


def test_remove_duplicates():
    assert remove_duplicates("hello world hello") == "hello world"


def test_slug():
    assert slug("Hello World") == "hello-world"
    assert slug("my blog post") == "my-blog-post"
