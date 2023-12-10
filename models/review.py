#!/usr/bin/python3
"""Modul define review class that inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class that represent review"""
    place_id = ""
    user_id = ""
    text = ""
