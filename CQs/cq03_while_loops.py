"""this is a program that will return the instances of a char in a str"""

__author__ = "730769565"


def num_instances(phrase: str, search_char: str) -> int:
    current_idx: int = 0
    total_occurences: int = 0
    while current_idx < len(phrase) - 1:
        if search_char == phrase[current_idx]:
            total_occurences += 1
        current_idx += 1
    print(total_occurences)
    return total_occurences


if __name__ == "__main__":
    num_instances(
        phrase=input("What is your phrase? "),
        search_char=input("What is the character you'd like to track? "),
    )
