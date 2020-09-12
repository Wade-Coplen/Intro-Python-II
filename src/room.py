# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.room_items = []
    def __str__(self):
        return f'You enter the {self.room_name}, {self.room_description}'
