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
        print(f"Invalid direction")
        return None

def find_unexplored_room(player, graph, last_direction):
    queue = Queue()
    visited_rooms = set()

    queue.enqueue([(reverse_direction(last_direction), player.current_room.id)])

    while queue.size() > 0:
        current_path = queue.dequeue()
        current_direction = current_path[-1][0]
        current_room_id = current_path[-1][1]

        if '?' in graph[current_room_id].values():
            path = []

            for p in current_path:
                path.append(p[0])
                print(f"p {p}")

            return path

        if current_room_id not in visited_rooms:
            visited_rooms.add(current_room_id)

            for direction, room_id in graph[current_room_id].items():
                path_copy = list(current_path)
                path_copy.append((direction, room_id))
                queue.enqueue(path_copy)


def bfs_paths(graph, start, goal, last_direction):
    queue = Queue()
    queue.enqueue(([reverse_direction(last_direction)], start))
    while queue:
        (path, vertex) = queue.dequeue()
        print(f"items in my graph {graph[vertex]}")
        for direction, room_id in graph[vertex].items():
            if room_id == goal:
                yield path + [direction]
            else:
                queue.enqueue((path + [direction], room_id))


def shortest_path(graph, start, goal, direction):
    try:
        return next(bfs_paths(graph, start, goal, direction))
    except StopIteration:
        return None
