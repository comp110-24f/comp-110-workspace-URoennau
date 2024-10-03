"""Mutating functions"""

__author__ = "730769565"


def manual_append(my_list: list[int], num: int) -> None:
    return my_list.append(num)


def double(my_list: list[int]) -> None:
    idx: int = 0
    while idx < len(my_list):
        my_list[idx] *= 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
