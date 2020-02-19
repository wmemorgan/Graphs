from random import randrange
from graph import Graph
from util import Queue


def earliest_ancestor(ancestors, starting_vertex):
    # Create graph
    graph = Graph()
    # Populate graph
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    # Do BFS on graph
    # make a queue
    queue = Queue()
    # enque a PATH to the starting vertex
    queue.enqueue([starting_vertex])

    longest_path_length = 1
    earliest_ancestor = -1
    # loop through queue
    while queue.size() > 0:
        # dequeue the next path
        path = queue.dequeue()
        # get the current vertex
        current_vertex = path[-1]
        # compare current path length with longest path length
        # compare current vertex with earliest ancestor
        if (len(path) >= longest_path_length and current_vertex < earliest_ancestor) or (len(path) > longest_path_length):
            # swap longest_path and earliest ancestor
            longest_path_length = len(path)
            earliest_ancestor = current_vertex

        neighbors = graph.vertices[current_vertex]
        print(f"NEIGHBORS: {neighbors}")
        # iterate through neighbors
        for neighbor in neighbors:
            # copy the path, add the neighbor to the
            path_copy = list(path)
            path_copy.append(neighbor)
            # for each one, add a PATH TO IT to our queue
            queue.enqueue(path_copy)
    print(f"PATH: {path}")
    print(f"EARLIEST ANCESTOR: {earliest_ancestor}")
    return earliest_ancestor
