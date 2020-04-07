from util import reverse_direction

class Player:
    def __init__(self, starting_room, prev_room=None, prev_direction=None):
        self.current_room = starting_room
        self.prev_room = prev_room
        self.prev_direction = prev_direction
    def travel(self, direction, show_rooms=False):
        self.prev_room = self.current_room
        self.prev_direction = reverse_direction(direction)
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print(f"Attempted to move {direction} in room {self.prev_room.id}")
            print("You cannot move in that direction.")
