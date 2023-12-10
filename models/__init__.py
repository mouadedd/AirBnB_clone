#!/usr/bin/python3
"""the init methode for the import model/modulenotfounderror"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
