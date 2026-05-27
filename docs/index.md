# Text Toolkit

![CI Pipeline](https://github.com/yashasm19/text-toolkit/actions/workflows/pipeline.yml/badge.svg)

A Python utility library with a fully automated CI/CD pipeline using GitHub Actions.

---

## Installation

```bash
git clone https://github.com/yashasm19/text-toolkit.git
cd text-toolkit
pip install -r requirements-dev.txt
```

---

## Functions

### word_count(text)
Count the frequency of each word in a string.
```python
word_count("hello world hello")
# {"hello": 2, "world": 1}
```

### reverse_words(text)
Reverse the order of words in a string.
```python
reverse_words("hello world")
# "world hello"
```

### is_palindrome(text)
Check if a string is a palindrome, ignoring spaces and case.
```python
is_palindrome("racecar")  # True
is_palindrome("hello")    # False
```

### truncate(text, max_len, suffix)
Truncate text to a maximum length.
```python
truncate("hello world", 8)
# "hello..."
```

### capitalize_words(text)
Capitalize the first letter of each word.
```python
capitalize_words("hello world")
# "Hello World"
```

### count_vowels(text)
Count the number of vowels in a string.
```python
count_vowels("hello world")
# 3
```

### remove_duplicates(text)
Remove duplicate words while preserving order.
```python
remove_duplicates("hello world hello")
# "hello world"
```

### slug(text)
Convert text to a URL-friendly slug.
```python
slug("Hello World")
# "hello-world"
```

---

## Running Tests

```bash
pytest --cov=toolkit
```

## Pipeline

Every push to main automatically runs:

- Lint check with flake8
- Unit tests on Python 3.10, 3.11, and 3.12
- Code coverage enforcement (80% minimum)
- Security scan with bandit
- Documentation deployment to GitHub Pages
