"""this program will allow me to continue to make list utility functions in python"""

__author__ = "730769565"


def only_evens(my_list: list[int]) -> list[int]:
    new_list: list[int] = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


def sub(my_list: list[int], start: int, end: int) -> list[int]:
    new_list: list[int] = []
    if start < 0:
        start = 0
    if end > len(my_list) - 1:
        end = len(my_list)
    for i in range(start, end):
        new_list.append(my_list[i])
    return new_list


def add_at_index(my_list, element: int, index: int) -> None:
    if index < 0 or index > len(my_list):
        raise IndexError("Index is out of bounds for the input list")
    my_list.append(None)
    for i in range(len(my_list) - 2, index - 1, -1):
        my_list[i + 1] = my_list[i]
    my_list[index] = element
    return None
