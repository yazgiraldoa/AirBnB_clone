#!/usr/bin/python3
"""
Class City that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City that inherits from BaseModel
    Attributes:
        state_id(str): state id
        name(str): city name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor of City"""
        super().__init__(*args, **kwargs)
