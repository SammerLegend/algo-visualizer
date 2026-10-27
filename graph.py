class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    def add_edge(self, source, destination):
        self.add_vertex(source)
        self.add_vertex(destination)

        if destination not in self.adjacency[source]:
            self.adjacency[source].append(destination)
        if source not in self.adjacency[destination]:
            self.adjacency[destination].append(source)
