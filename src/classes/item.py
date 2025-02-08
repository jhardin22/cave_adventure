import json


class Item:
    def __init__(self, name, description, is_key, color):
      self.name = name
      self.description = description
      self.is_key = False
      self.color = color