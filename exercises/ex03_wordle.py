"""a program that is similar to the online game that prompts its user to guess a secret word with limited guesses and few hints"""

__author__ = "730769565"


def input_guess(secret_word_len: int) -> str:
    """prompts the user for an n character word"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """checks to see if char in word"""
    assert (
        len(char_guess) == 1
    )  # I didn't know about this "assert" function which is a good thing to learn!
    idx: int = 0
    while idx != len(secret_word):
        if secret_word[idx] == char_guess:
            return True
        idx += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """compares two strings of equal length"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    return_str: str = ""  # create an empty string that will be filled later
    while idx != len(guess):
        if guess[idx] == secret_word[idx]:  # check for equality of indices
            return_str += GREEN_BOX
        elif contains_char(secret_word, guess[idx]):
            return_str += YELLOW_BOX
        else:
            return_str += WHITE_BOX
        idx += 1
    return return_str


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 0
    won: bool = False
    while (
        turn < 6
    ) and not won:  # increments turn-count up to 6 and checks to see that the "False" value of won is still present in order to enter the loop
        turn += 1
        print(f"=== Turn === {turn}/6 ===")
        current_guess: str = input_guess(len(secret))
        current_emoji_output = emojified(
            current_guess, secret
        )  # creating a variable called "current_emoji_output" so that I dont have to copy-paste the code
        print(current_emoji_output)
        if (
            current_guess == secret
        ):  # checks to see if the user has guessed the correct word
            won = True
            print(f"You won in {turn}/6 turns!")
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
