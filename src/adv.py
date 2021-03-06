from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
player = Player("George", room['outside'])
torch = Item("Torch", "To guide you")
satchel = Item("Satchel", "A bag to carry what you find")


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
print(f'You are currently: {player.current_room.room_name}')
# * Prints the current description (the textwrap module might be useful here).
print(f'{player.current_room.room_description}')
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.


   
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    direction = input('Which direction will you choose? Enter n = North, s = South, e = East, w = West:')
    pickupItem = 
    
    if direction == 'n':
        print(f'{player.current_room.n_to}')
    else:
        print('You must not be afraid. Go forward bravely!')
    if player.current_room:
        print(player.current_room.room_items)
   
    if direction == 'q':
        print('Game over')
    if player.current.room == 
        break