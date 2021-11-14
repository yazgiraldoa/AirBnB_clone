#!/usr/bin/python3
"""
Class FileStorage that serializes instances to
a JSON file and deserializes JSON file to instances
"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class FileStorage():
    """
    class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    Attributes:
        __file_path(str): path to the JSON file
        __objects(dict): dictionary that will store
        all objects by <class name>.id
    """
    __file_path = "data.json"
    __objects = {}

    def all(self):
        """Method that returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        Method that sets the obj in __objects
        with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Method that serializes __objects to the JSON file"""
        dic_to_save = {}

        for key in self.__objects.keys():
            dic_to_save[key] = self.__objects.get(key).to_dict()

        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(dic_to_save, f)

    def reload(self):
        """
        Method that deserializes
        the JSON file to __objects
        """
        if exists(self.__file_path):
            try:
                with open(self.__file_path, mode='r', encoding="utf-8") as f:
                    json_str = f.read()
                    dic = json.loads(json_str)

                    for k, v in dic.items():
                        self.__objects[k] = eval(f"{v.get('__class__')}(**v)")
            except Exception:
                pass
