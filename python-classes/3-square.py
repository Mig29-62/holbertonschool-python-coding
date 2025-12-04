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
            self._size = size

    @property
    def size(self):
        return self._size

    def area(self):
        return self._size**2

    @size.setter
    def size(self, value):
        if not isinstance(self._size, int):
            raise TypeError("size must be an integer")
        else:
            self._size = value