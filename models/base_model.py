#!/usr/bin/python3
"""defines basemodel class for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    The BaseModel class serves as the base class for other classes.

    Attributes:
        id (str): The unique identifier for each instance.
        created_at (datetime): The timestamp representing the creation\
            time of the instance.
        updated_at (datetime): The timestamp representing the last update\
            time of the instance.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    if key == "created_at":
                        kwargs[key] = datetime\
                            .strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    elif key == "updated_at":
                        kwargs[key] = datetime\
                            .strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute and saves the instance\
            to the storage dict.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary.

        Returns:
            dict: A dictionary containing the instance attributes plus\
                <__class__.__name__> added
        """
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
