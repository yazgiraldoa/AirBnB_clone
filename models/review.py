#!/usr/bin/python3
"""
Class Review that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review that inherits from BaseModel
    Attributes:
        place_id(str): id of the place
        user_id(str): id of the user
        text(str): review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor of Review"""
        super().__init__(*args, **kwargs)
