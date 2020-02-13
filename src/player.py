# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    # player should have a name
    def __init__(self, name, start_room):
        self.name = name
        self.current_room = start_room
        #self.inventory = []
        #self.score = 0
    def travel(self, direction):
        #Player should be able to move in a direction 
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print('You cannot move in that direction')
