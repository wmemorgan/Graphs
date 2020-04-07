from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue, select_exit, reverse_direction, find_unexplored_room

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

print(f"NUMBER OF ROOMS: {len(room_graph)}")
print(f"ROOM_GRAPH: {room_graph}")

# Create an exploration graph
explore_graph = {}

"""Initial Exploration with DFS"""
# Create a stack
stack = Stack()
# Add starting room to the stack
stack.push(player.current_room)

while len(explore_graph) < len(room_graph):
    # while stack.size() > 0:
    current_room = stack.pop()
    room_exits = player.current_room.get_exits()

    # Check if current room is in explore_graph:
    #print(f"CURRENT ROOM: {current_room.id}")
    if current_room.id not in explore_graph:
        # Add to explore_graph

        explore_graph[current_room.id] = {exit: '?' for exit in room_exits}
        print(
            f"explore_graph[current_room.id]: {current_room.id}: {explore_graph[current_room.id]}")

        print(f"ROOM EXITS {room_exits}")

    # Randomly select an exit
    possible_exits = [
        direction for (direction, room_id) in explore_graph[current_room.id].items() if room_id == '?']

    if len(explore_graph[current_room.id].keys()) == 1 and len(possible_exits) > 0:
        direction = player.current_room.get_exits()[0]
        print(f"EXITS: {direction}")
        traversal_path.append(direction)
        prev_room = current_room
        player.travel(direction)
        stack.push(player.current_room)

    elif len(possible_exits) > 0:
        print(f"POSSIBLE EXITS: {possible_exits}")
        random_exit = random.choice(possible_exits)
        #print(f"random_exit: {random_exit}")
        traversal_path.append(random_exit)
        prev_room = current_room
        player.travel(random_exit)
        explore_graph[prev_room.id][random_exit] = player.current_room.id
        stack.push(player.current_room)

    else:
        print(f"graph before BFS: {explore_graph}")
        print(f"starting room before BFS: {player.current_room.id}")
        find_exit = find_unexplored_room(player, explore_graph)
        print(f"UNEXPLORED PATH: {find_exit}")

        # if len(find_exit) == 1:
        #     find_exit = find_unexplored_room(player, explore_graph)

        if find_exit:
            for step in find_exit:
                print(f"starting in room {player.current_room.id}")
                print(f"GOING {step}")
                traversal_path.append(step)
                player.travel(step)
                print(f"In room {player.current_room.id}")
                print(f"PREVIOUS ROOM {player.prev_room.id}")

                if player.current_room.id in explore_graph:
                    explore_graph[player.prev_room.id][step] = player.current_room.id

                else:
                    print(
                        f"ADD ROOM {player.current_room.id} TO STACK")
                    stack.push(player.current_room)
                    break

            print(f"ending room {player.current_room.id}")
            print(f"graph after BFS: {explore_graph}")

    print(f"DEAD END AT ROOM {player.current_room.id} KEEP IT GOING")
    stack.push(player.current_room)
    print(
    f"Number of rooms in explore_graph: {len(explore_graph)}")
    # print(f"current stack {stack.stack}")



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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
