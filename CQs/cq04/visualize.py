""""""

__author__ = "730769565"

from concatenation import concat
from coordinates import get_coords

x: str = "123"
y: str = "abc"
if __name__ == "__main__":
    print(concat(x, y))
    get_coords(x, y)
