import random

# Note: This Queue class is sub-optimal. Why?
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



def select_exit(exits):
    possible_exits = [k for (k, v) in exits.items() if v == '?']
    
    try:
        random_exit = random.choice(possible_exits)
    except IndexError:
        return None
    return random_exit

def reverse_direction(direction):
    directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    try:
        return directions[direction]
    except KeyError:
        print(f"Invalid direction: {direction}")
        return None

def find_unexplored_room(player, graph):
    queue = Queue()
    visited_rooms = set()
    queue.enqueue([(player.prev_direction, player.current_room.id)])

    while queue.size() > 0:
        current_path = queue.dequeue()
        last_room_id = current_path[-1][1]

        if '?' in graph[last_room_id].values():
            path = 
            # print(f"FOUND SOMETHING: {graph[last_room_id]}")
            # print(f"current_path: {current_path}")
            # unexplored_exit = [k for (k, v) in graph[last_room_id].items() if v == '?']
            # unexplored_path = [direction for (
            #     direction, room_id) in current_path if direction is not None]
            # unexplored_path.extend(unexplored_exit)
            # print(f"UNEXPLORED PATH: {unexplored_path}")
            # return unexplored_path


        if last_room_id not in visited_rooms:
            visited_rooms.add(last_room_id)

            for direction, room_id in graph[last_room_id].items():
                path_copy = list(current_path)
                path_copy.append((direction, room_id))
                queue.enqueue(path_copy)


        #     pass




    
