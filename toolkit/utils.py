def word_count(text: str) -> dict:
    """Count word frequency in a string."""
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def reverse_words(text: str) -> str:
    """Reverse the order of words in a string."""
    return " ".join(text.split()[::-1])


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome (ignores spaces, case)."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Truncate text to max_len characters."""
    if len(text) <= max_len:
        return text
    return text[:max_len - len(suffix)] + suffix
