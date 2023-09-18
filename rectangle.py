#!/usr/bin/python3
"""Module that defines Rectangle class and is base subclass"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle instance

        Args:
            width (int): width of the rectangle
            height (int): height of rectangle
            x (int): the x-coordinate
            y (int): the y-coordinate
            id (int): identifier for the instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Fetch width of rectangle"""
        return self.__width
