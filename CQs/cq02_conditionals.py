"""this program is a simple number number guessing game"""

__author__ = "730769565"


def guess_a_number() -> None:
    """this is a cool function for guessing the number"""
    secret = 7
    response = int(input("Guess a number:"))
    print("Your guess was " + str(secret))
    if response == secret:
        print("You got it!")
    elif response < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


guess_a_number()

if __name__ == "__main__":
    guess_a_number()
