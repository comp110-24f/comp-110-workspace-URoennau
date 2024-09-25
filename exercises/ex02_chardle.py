"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730769565"


def input_word() -> str:
    """prompts for the key word"""  # what's up! Welcome to me comments :)
    fc_word: str = input(
        "Enter a 5-character word: "
    )  # fc_word stands for "five character word"
    if (len(fc_word) < 5) or (
        len(fc_word) > 5
    ):  # I decided to have a conjuction in my if statement to make it less cumbersome
        print("Error: Word must contain 5 characters.")
        exit()
    return fc_word


def input_letter() -> str:
    """prompts for the target letter"""  # including docstrings is a habit I'd like to get used to
    target_letter = input("Enter a single character: ")
    if len(target_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return target_letter


def contains_char(word: str, letter: str) -> None:
    """checks to see if the target letter is in the word"""
    print(f"Searching for {letter} in {word}")
    num_of_letters_in_word: int = 0
    if (
        letter == word[0]
    ):  #  manually checks for the indices 5 times because I'm not allowed to use a counter or a for-loop :(
        num_of_letters_in_word += 1
        print(f"{letter} found at index 0")
    if letter == word[1]:
        num_of_letters_in_word += 1
        print(f"{letter} found at index 1")
    if letter == word[2]:
        num_of_letters_in_word += 1
        print(
            f"{letter} found at index 2"
        )  # at this point, the copy and pasting was hurting my soul a little bit...
    if letter == word[3]:
        num_of_letters_in_word += 1
        print(f"{letter} found at index 3")
    if letter == word[4]:
        num_of_letters_in_word += 1
        print(f"{letter} found at index 4")
    if num_of_letters_in_word == 0:
        print(f"No instances of {letter} found in {word}")
    elif num_of_letters_in_word == 1:
        print(f"{num_of_letters_in_word} instance of {letter} found in {word}")
    else:
        print(f"{num_of_letters_in_word} instances of {letter} found in {word}")


def main() -> None:
    """combines all the complementary functions for the program to run"""
    contains_char(word=input_word(), letter=input_letter())


if (
    __name__ == "__main__"
):  # allows me to use thee fuctions defined above in other programs without running main()
    main()
