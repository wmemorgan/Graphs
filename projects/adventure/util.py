import random

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def reverse_direction(direction):
    directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    try:
        return directions[direction]
    except KeyError:
        print(f"Invalid direction: {direction}")
        return None


def find_unexplored_room(player, graph):
    """Find shortest path to unexplored rooms"""

    queue = Queue()
    visited_rooms = set()
    starting_room_id = player.current_room.id
    queue.enqueue([(None, starting_room_id)])

    while queue.size() > 0:
        current_path = queue.dequeue()
        current_room_id = current_path[-1][1]

        if '?' in graph[current_room_id].values():
            # Create and return directions
            unexplored_exit = [
                direction for (direction, room_id) in graph[current_room_id].items() if room_id == '?']
            unexplored_path = [direction for (
                direction, room_id) in current_path if direction is not None]
            unexplored_path.extend(unexplored_exit)

            return unexplored_path

        if current_room_id not in visited_rooms:
            visited_rooms.add(current_room_id)
            for (direction, room_id) in graph[current_room_id].items():
                pair = (direction, room_id)
                path_copy = list(current_path)
                path_copy.append(pair)
                queue.enqueue(path_copy)

    print(f"No current path: {current_path}")
    return None
