class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, src, dest):
        if src >= 0 and src < self.num_vertices and dest >= 0 and dest < self.num_vertices:
            self.adj_matrix[src][dest] = 1
            self.adj_matrix[dest][src] = 1

    def print_graph(self):
        for row in self.adj_matrix:
            print(row)

g = Graph(4)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

g.print_graph()
