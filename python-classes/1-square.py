#!/usr/bin/python3
"""we define the class square and raise errors about size"""


class Square:
    """specific errors have specific outputs"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
