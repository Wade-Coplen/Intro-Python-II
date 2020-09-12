class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def take_item(self):
        print(f'You have picked up {self.name}')
    def drop_item(self):
        print(f'You have dropped {self.name}')