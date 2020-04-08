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


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

# ancestors
##  [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
def earliest_ancestor(ancestors, starting_node):
    # build a graph
    graph = Graph()
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    # BFS
    queue = Queue()
    queue.enqueue([starting_node])

    longest_path_length = 1
    earliest_ancestor = -1

    while queue.size() > 0:
        path = queue.dequeue()
        current_node = path[-1]

        if len(path) >= longest_path_length and current_node < earliest_ancestor:
                longest_path_length = len(path)
                earliest_ancestor = current_node

        if len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        neighbors = graph.vertices[current_node]
        print(neighbors)
        for ancestor in neighbors:
            path_copy = list(path)
            path_copy.append(ancestor)
            queue.enqueue(path_copy)

    print(path)
    print(earliest_ancestor)
    return earliest_ancestor
