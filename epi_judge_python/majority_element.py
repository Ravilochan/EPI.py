from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    majority, count = None, 0
    for it in stream:
        if count == 0:
            majority, count = it, 1
        elif it == majority:
            count += 1
        else:
            count -= 1
    return majority


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
