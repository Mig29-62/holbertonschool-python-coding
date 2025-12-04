#!/usr/bin/python3
"""we define the class square and raise errors about size"""


class Square:
    """we define specific errors and according to that print specific messages"""

    def __init__(self, size=0):
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size=size