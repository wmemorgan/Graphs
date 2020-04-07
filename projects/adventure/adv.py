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
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

print(f"NUMBER OF ROOMS: {len(room_graph)}")

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
    available_exits = player.current_room.get_exits()

    # Check if current room is in explore_graph:
    if current_room and current_room.id not in explore_graph:
        # Add to explore_graph
        explore_graph[current_room.id] = {exit: '?' for exit in available_exits}
        # Randomly select an exit
        random_exit = select_exit(explore_graph[current_room.id])

        # if random_exit:
        #     #print(f"random_exit: {random_exit}")
        traversal_path.append(random_exit)
        prev_room = current_room
        player.travel(random_exit)
        explore_graph[prev_room.id][random_exit] = player.current_room.id
        stack.push(player.current_room)


    else:
        if current_room:
            # Randomly select an exit
            random_exit = select_exit(explore_graph[current_room.id])

            if random_exit:
                traversal_path.append(random_exit)
                prev_room = current_room
                player.travel(random_exit)
                explore_graph[prev_room.id][random_exit] = player.current_room.id
                stack.push(player.current_room)
            else:
                print(f"No more '?' exits")
                print(f"where am I?: room {current_room.id}")
                print(
                    f"and where have I been? room {player.prev_room.id} from {player.prev_direction} direction")
                print(f"what is already in graph? : {explore_graph}")
                print(f"STARTING ROOM: {player.current_room.id}")
                print(f"AVAILABLE EXITS: {explore_graph[player.current_room.id]}")
                something = find_unexplored_room(player, explore_graph)

                if something:
                    for step in something:
                        traversal_path.append(step)
                        prev_room = player.current_room
                        player.travel(step)
                        if prev_room == player.current_room:
                            break
                        
                        if player.current_room.id in explore_graph:
                            explore_graph[prev_room.id][step] = player.current_room.id
                        else:
                            print(f"MISSING ROOM {player.current_room.id} ADDING IT TO STACK")
                            stack.push(player.current_room)
                            break
                print(f"FINAL GRAPH STATUS: {explore_graph}")
                print(f"where am I?: room {current_room.id}")
                print(
                    f"and where have I been? room {player.prev_room.id} from {player.prev_direction} direction")
                        # explore_graph[prev_room.id][random_exit] = player.current_room.id
                        # stack.push(player.current_room)

                    # else:
                    #     print(f"CRAPPED OUT AGAIN: {something}")

        else:
            break
            
   





# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
