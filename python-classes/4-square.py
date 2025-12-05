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
        if not isinstance(self._size, int):
            raise TypeError("size must be an integer")
        else:
            return self._size

    def area(self):
        return self._size**2

    @size.setter
    def size(self, value):
        if not isinstance(self._size, int):
            raise TypeError("size must be an integer")
        else:
            self._size = value

    def my_print(self):
        if self.size == 0:
            print('\n',end='')
        for i in range(0,self.size):
            for j in range(0,self.size):
                print('#',end='')
            print('\n',end='')
