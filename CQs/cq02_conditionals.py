"""this program is a simple number number guessing game"""

__author__ = "730769565"


def guess_a_number() -> None:
    """this is a cool function for guessing the number"""
    secret = 7
    response = input("Guess a number: ")
    print("Your guess was " + response)
    if int(response) == secret:
        print("You got it!")
    elif int(response) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
