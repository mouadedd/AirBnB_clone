#!/usr/bin/python3
"""Base model task 3"""

from uuid import uuid4
from datetime import datetime
import models

time_form = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """
    a class BaseModel that defines all common attributes/methods
    for other classes"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and \
               type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs
                                                    ["created_at"], time_form)
            if hasattr(self, "updated_at") and \
               type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs
                                                    ["updated_at"], time_form)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """the printed representation of tha base model"""
        cl_name = self.__class__.__name__
        return "[{}]({}) {}".format(cl_name, self.id, self.__dict__)

    def save(self):
        """the updated datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """kwargs, dictionary containing items of __dict__"""
        ret_dc = self.__dict__.copy()
        ret_dc["created_at"] = self.created_at.isoformat()
        ret_dc["updated_at"] = self.updated_at.isoformat()
        ret_dc["__class__"] = self.__class__.__name__
        return ret_dc
