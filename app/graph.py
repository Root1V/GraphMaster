class Edge:
    def __init__(self, vertex1, vertex2) -> None:
        self.v1 = vertex1
        self.v2 = vertex2

    def get_v1(self):
        return self.v1

    def get_v2(self):
        return self.v2

    def __str__(self) -> str:
        return f"Arista: {self.v1.get_name()} ---> {self.v2.get_name()}"


class Vertex:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self) -> str:
        return f"({self.name})"


class DiGraph:
    def __init__(self) -> None:
        self.dictionary = {}

    def add_vertex(self, vertex: Vertex):

        if vertex in self.dictionary:
            return "Vertex already in Graph"

        self.dictionary[vertex] = []

    def add_edges(self, edge: Edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()

        if v1 not in self.dictionary:
            raise ValueError(f"Vertex: {v1.get_name()} not in graph")

        if v2 not in self.dictionary:
            raise ValueError(f"Vertex: {v2.get_name()} not in graph")

        self.dictionary[v1].append(v2)

    def is_vertex_in(self, vertex: Vertex):
        return vertex in self.dictionary

    def get_vertex(self, vertex_name):

        for v in self.dictionary:
            if vertex_name == v.get_name():
                return v

        print(f"Vertex: {vertex_name} does not exists")

    def get_neighbours(self, vertex: Vertex):
        return self.dictionary[vertex]

    def __str__(self) -> str:

        all_edges = ""
        for v1 in self.dictionary:
            for v2 in self.dictionary[v1]:
                all_edges += v1.get_name() + " -----> " + v2.get_name() + "\n"

        return all_edges


class UnDiGraph(DiGraph):
    def add_edges(self, edge: Edge):
        super().add_edges(edge)
        edge_back = Edge(edge.get_v2(), edge.get_v1())
        super().add_edges(edge_back)
