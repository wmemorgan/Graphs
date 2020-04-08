from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue, find_unexplored_room

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# EXAMPLE: traversal_path = ['n', 'n']
traversal_path = []

# Create an exploration graph
explore_graph = {}

"""Initial Exploration with DFS"""
# Create a stack
stack = Stack()
# Add starting room to the stack
stack.push(player.current_room)

while len(explore_graph) < len(room_graph):
    # Explore rooms using DFS
    current_room = stack.pop()
    room_exits = player.current_room.get_exits()

    # Check if current room is in explore_graph:
    if current_room.id not in explore_graph:
        # Add to explore_graph
        explore_graph[current_room.id] = {exit: '?' for exit in room_exits}

    # Travel through unexplored exits
    possible_exits = [
        direction for (direction, room_id) in explore_graph[current_room.id].items() if room_id == '?']

    if len(possible_exits) > 0:
        # Randomly select an exit
        random_exit = random.choice(possible_exits)
        # Map out traversal path
        traversal_path.append(random_exit)
        # Travel through and map out room exits
        prev_room = current_room
        player.travel(random_exit)
        explore_graph[prev_room.id][random_exit] = player.current_room.id
        # Add the next room to the stack
        stack.push(player.current_room)

    else:
        # Find shortest path to unexplored exits
        find_exit_path = find_unexplored_room(player, explore_graph)

        # Append unexplored exits shortest path to main traversal path
        if find_exit_path:
            for step in find_exit_path:
                traversal_path.append(step)
                player.travel(step)

                if player.current_room.id not in explore_graph:
                    stack.push(player.current_room)
                    break

    # Handle dead ends
    stack.push(player.current_room)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
"""
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
"""
