__author__ = 'tianwei'
from pymongo import Connection
import json


class BaseModel:
    def __init__(self):
        pass
    def save(self):
        pass

    def to_dict(self):
        for name, value in vars(self).items():
            print name,value