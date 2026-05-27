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


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in text.split())


def count_vowels(text: str) -> int:
    """Count the number of vowels in a string."""
    return sum(1 for char in text.lower() if char in "aeiou")


def remove_duplicates(text: str) -> str:
    """Remove duplicate words from a string, preserving order."""
    seen = set()
    result = []
    for word in text.split():
        if word.lower() not in seen:
            seen.add(word.lower())
            result.append(word)
    return " ".join(result)


def slug(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    return "-".join(text.lower().split())
