# Contributing to Text Toolkit

Thank you for your interest in contributing!

## Setup

1. Clone the repo
   git clone https://github.com/yashasm19/text-toolkit.git

2. Install dependencies
   pip install -r requirements-dev.txt

3. Run tests
   pytest --cov=toolkit

## Guidelines

- All new functions must have a docstring
- All new functions must have at least one test
- Code must pass flake8 linting
- Coverage must stay above 80%

## Pull Request Process

1. Create a new branch for your feature
2. Write your code and tests
3. Push and open a Pull Request to main
4. CI pipeline must pass before merging
