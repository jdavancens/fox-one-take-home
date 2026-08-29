# PART 2: PYTHON (STANDARD LIBRARY ONLY)

Use Python 3 and the standard library only.

General Instructions:

* Write clear, idiomatic Python.
* Use type hints where reasonable.
* Add brief comments or docstrings for non‑obvious logic.
* Focus on approach and reasoning, not just the final answer.

This test is not meant to be purely tactical. We care about:

* How you break down problems
* How you reason through edge cases
* How you explain alternative approaches

## TASK 1: STRING & COLLECTIONS

Implement: `most_common_word(text: str, stopwords: set[str] | None = None) -> str | None`

Expectations:

* Normalize input text appropriately
* Handle empty input and stopwords
* Return None when no valid result exists

## TASK 2: DATA STRUCTURES & ALGORITHMS

* Implement: `merge_intervals(intervals: list[list[int]]) -> list[list[int]]`

Expectations:

* Correctly merge overlapping intervals
* Handle unsorted input
* Explain your approach briefly in comments or docstring

## TASK 3: OOP DESIGN & API THINKING

Create a Logger class with the following methods:
```
log(message: str) -> None
get_logs() -> list[str]
search(query: str) -> list[str]
```
Expectations:

Clean, simple interface
Reasonable internal data structure choices
Clear separation of responsibilities

## TASK 4: DEBUGGING & REFACTORING

You are given a broken Fibonacci function.

* Identify what is wrong
*Fix the function

Provide:

* An iterative version
* A memoized version

Expectations:

* Explain why each version behaves differently
* Compare tradeoffs briefly (performance, readability)

## TASK 5: HASHING & GROUPING

Implement: `group_anagrams(words: list[str]) -> list[list[str]]`

Expectations:

* Correct grouping
* Efficient use of data structures
* Clear logic

## SUBMISSION

Please provide:

* A GitHub repository link for Part 1 (frontend)
* A Python file or repository for Part 2
* Clear instructions to run your code
* We value clarity, reasoning, and fundamentals over advanced frameworks or clever tricks.