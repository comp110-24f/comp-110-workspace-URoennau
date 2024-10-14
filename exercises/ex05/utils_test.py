"""this program will test the functions in 'utils.py'"""

__author__ = "730769565"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_empty_list():
    """tests if only_evens returns an empty list when the input is also and empty list"""
    assert only_evens([]) == []


def test_only_evens_mixed_parity():
    """tests if only_evens returns only even numbers from a list of mixed parity numbers"""
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_only_evens_no_mutation():
    """tests to see if the original input was mutated"""
    input: list[int] = [1, 2, 3, 4, 5, 6]
    only_evens(input)
    assert input == [1, 2, 3, 4, 5, 6]


def test_sub_empty_list():
    """tests if sub returns an empty list if the input is empty too"""
    assert sub([], 0, 1) == []


def test_sub_valid_range():
    """tests if sub correctly returns a sublist with indices in range"""
    assert sub([10, 20, 30, 40, 50], 1, 3) == [20, 30]


def test_sub_no_mutation():
    """tests to see if the original input was mutated"""
    input = [10, 20, 30, 40, 50]
    sub(input, 1, 3)
    assert input == [10, 20, 30, 40, 50]


def test_add_at_index_empty_list():
    """tests if add_at_index adds an element to empty list"""
    input = []
    add_at_index(input, 99, 0)
    assert input == [99]


def test_add_at_index_valid_index():
    """tests if add_at_index adds an element at specific index"""
    input = [1, 2, 4, 5]
    add_at_index(input, 3, 2)
    assert input == [1, 2, 3, 4, 5]


def test_add_at_index_mutation():
    """tests to see if function is mutated"""
    input = [1, 2, 3]
    add_at_index(input, 4, 2)
    assert input == [1, 2, 4, 3]
