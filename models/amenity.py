#!/usr/bin/python3
"""
Class Amenity that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class Amenity that inherits from BaseModel
    Attributes:
        name(str): amenity name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor of Amenity"""
        super().__init__(*args, **kwargs)
