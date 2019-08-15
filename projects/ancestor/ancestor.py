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


# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

class Graph:
    ''' Represent a graph as a dictionary of vertices mapping labels to edges'''
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            # Error
             pass
    def add_edge(self, vertex_from, vertex_to):
        if vertex_from in self.vertices and vertex_to in self.vertices:
            self.vertices[vertex_from].add(vertex_to)
        else:
            # Error
            pass


def earliest_ancestor(ancestors, starting_node):
    # Make a graph
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # add edges
        graph.add_edge(pair[1], pair[0])

    # Traverse the graph with BFS
    q = Queue()
    q.enqueue([starting_node])    

    max_path_length = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        node = path[-1]

        # We keep the path if it's longer OR 
        if ((len(path) > max_path_length) or
           (len(path) == max_path_length and node < earliest_ancestor)):
            earliest_ancestor = node 
            max_path_length = len(path)

        for neighbor in graph.vertices[node]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor


# Steps we need to do:
# Make a graph

# Traverse the graph with BFS
# Looking for shortest paths between any two nodes
# keep track of the lengths of these paths and 
# Return where the longest path ends
# if there are no parents return -1
# if it is a tie, return lowest node number

# Key words for problem solving:
# Relationships -- This is probably a graph problem
# Farthest distance --- 
# Integer Id -- Node/Vertices/Vertex
# Parent child pair --- Edges - 
# Only looking up to an ancestor -- Directional 
# Not all relationships are the same

