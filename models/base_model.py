#!/usr/bin/python3
"""
Class BaseModel that defines all common attributes/methods for other classes
"""
import uuid
import datetime
import models


class BaseModel():
    """
    Class BaseModel that defines all common
    attributes/methods for other classes
    Attributes:
        id(str): unique id for each object.
        created_at(datetime): current datetime when
        an instance is created
        updated_at(datetime): current datetime when
        an instance is created and it will be updated
    """

    def __init__(self, *args, **kwargs):
        """Constructor of Base Model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String representation of class as
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Method that updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Method that returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()

        return dic
