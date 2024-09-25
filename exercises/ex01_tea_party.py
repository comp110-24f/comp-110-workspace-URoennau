"""this program prompts the user for a number of party guests and return the required number of teabags, treats, and the total cost"""

__author__: str = "730769565"


def main_planner(guests: int) -> None:
    """entrypoint to the program"""
    print(
        f"A Cozy Tea Party for {guests} people!"
    )  # these curly braces allow me to format the string to include active calling of functions
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(
        f"Cost: ${cost(tea_bags(people=guests), treats(people=guests))}"
    )  # this nested function prints out the total cost by running "tea_bags()" and "treats()" one more time as arguments


def tea_bags(people: int) -> int:
    """calculates necessary number of teabags"""
    return people * 2


def treats(people: int) -> int:
    """calculates number of treats needed based on number of tea bags had"""
    return int(1.5 * (tea_bags(people=people)))


def cost(tea_count: int, treat_amount: int) -> float:
    """calculates the total cost"""
    return tea_count * 0.5 + treat_amount * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
