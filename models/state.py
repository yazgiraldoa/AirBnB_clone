#!/usr/bin/python3
"""
Class State that inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Class State that inherits from BaseModel
    Attributes:
        name(str): State name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor of State"""
        super().__init__(*args, **kwargs)
