#!/usr/bin/python3
"""Define a square class based on rectangle"""




Rectangle = __import__('9-rectangle').Rectangle




class Square(Rectangle):
    """Define inhereted BaseGeometry class Rectangle"""
    def __init__(self, size):
        """Initialize"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
