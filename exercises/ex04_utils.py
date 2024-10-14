"""this program implements some helpful functions to work with lists in python"""

__author__ = "730769565"


def all(my_list: list[int], num: int) -> bool:
    idx: int = 0
    if len(my_list) == 0:
        return False
    while idx < len(my_list):
        if my_list[idx] != num:
            return False
        else:
            idx += 1
    return True


def max(my_list2: list[int]) -> int:
    if len(my_list2) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    largest: int = -10000
    while idx < len(my_list2):
        if my_list2[idx] > largest:
            largest = my_list2[idx]
        idx += 1
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    idx: int = 0
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True


def extend(a: list[int], b: list[int]) -> None:
    main_idx: int = 0
    while main_idx < len(b):
        a.append(b[main_idx])
        main_idx += 1
    return None
