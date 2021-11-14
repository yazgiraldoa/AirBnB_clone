#!/usr/bin/python3
"""
Class Place that inherits from BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class Place that inherits from BaseModel
    Attributes:
        city_id(str): id of the city
        user_id(str): id of the user
        name(str): State name
        description(str): description of the place
        number_rooms(int): number of rooms in the place
        number_bathrooms(int): number of bathrooms in the place
        max_guest(int): max number of guest in the place
        price_by_night(int): price by night
        latitude(float): latitude
        longitude(float): longitude
        amenity_ids(list of str): amenity ids

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Constructor of Place"""
        super().__init__(*args, **kwargs)
