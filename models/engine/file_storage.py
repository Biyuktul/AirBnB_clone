#!/usr/bin/python3
"""file storage engine for the AirBnB clone project"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Represents a simple file-based storage system for managing instances.

    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary to store instances in\
            the format {'class_name.id': instance}.
    """

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """
        Returns the dictionary of all objects stored.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj : The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves the objects in the storage dictionary to a JSON file.
        """
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as fh:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, fh)

    def reload(self):
        """
        Reloads objects from the JSON file into the storage dictionary.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as fh:
                data = json.load(fh)
                if not data:
                    return
                for key, value in data.items():
                    class_name = value["__class__"]
                    attrs = {}
                    for k, v in value.items():
                        if k != "__class__":
                            attrs[k] = v
                    instance = eval(class_name)(**attrs)
                    self.new(instance)
