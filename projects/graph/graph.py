"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

# Vertex
# Identifier (int, name, string, etc.)
# List of edges...

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else: 
            print('warning: vertex does not exist')
        # TODO: 
    def add_edge(self, vertex_from, vertex_to):
        """
        Add a directed edge to the graph.
        # TODO: confirm intent is direction should be from V1 to V2
        """
        if vertex_from in self.vertices and vertex_to in self.vertices:
            self.vertices[vertex_from].add(vertex_to) 
        else:
            print('Warning, supplied vertex does not exist')
        
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        found = [starting_vertex, ]
        while q.size() > 0:
            for vertex in self.vertices[q.queue[0]]:
                if vertex not in found:
                    q.enqueue(vertex)
                    found.append(vertex)
            q.dequeue()

        # print(f'BFT: {found}')
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        found = []
        while s.size() > 0:
            current = s.pop()
            if current not in found:
                found.append(current)
                for next_vert in self.vertices[current]:
                    s.push(next_vert)
        print(f'DFT {found}')


        # create an empty set to store visited nodes
        # visited = set()        
        # # Create an empty stack and push the starting vertex
        # s = Stack()
        # s.push(starting_vertex)
        # # while the stack is not empty
        # while s.size() > 0:
        #     # pop the first vertex
        #     v = s.pop()
        #     # if the vertex has not been visited
        #     if v not in visited:
        #         # add that vertex to the visited set
        #         visited.add(v)
        #         #Add all neighbors of that vertex to top of stack
        #         for neighbors in self.vertices[v]:
        #             s.push(neighbors)

    def dft_recursive(self, starting_vertex, visited=[]):
        visited.append(starting_vertex)
        # print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)
        return visited


    # def dft_recursive(self, starting_vertex, visited=None):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.
    #     This should be done using recursion.
    #     """
    #     if visited is None:
    #         visited = set()
    #     visited.add(starting_vertex)

    #     for neighbors in self.vertices[starting_vertex]:
    #         if neighbors not in visited:
    #             self.dft_recursive(neighbors, visited)
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])

        found = []
     
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            if v not in found:
                if v == destination_vertex:
                    return path
                found.append(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        return None


        
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # s = Stack()
        # s.push([starting_vertex])
        # found = []
     
        # while s.size() > 0:
        #     path = s.pop()
        #     v = path[-1]

        #     if v not in found:
        #         if v == destination_vertex:
        #             return path
        #         found.append(v)
        #         for next_vert in self.vertices[v]:
        #             new_path = list(path)
        #             new_path.append(next_vert)
        #             s.push(new_path)
        # return None
        s = Stack()
        s.push([starting_vertex])
        visited = []

        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.append(vertex)
            for neighbor in self.vertices[vertex]:
                new_path = list(path)
                new_path.append(neighbor)
                s.push(new_path)

        return None



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(f'Recursive: {graph.dft_recursive(1)}')

    #Test BFS
    print(f'Testing results {graph.bfs(1, 6)}')

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
