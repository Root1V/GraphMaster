from app.graph import DiGraph, UnDiGraph, Vertex, Edge
from app.SearchAlg import DFS

if __name__ == "__main__":
    print(" ==== START App GenAI =================================\n")

    g = UnDiGraph()

    for v in ("l", "i", "e", "s", "v", "a"):
        g.add_vertex(Vertex(v))

    g.add_edges(Edge(g.get_vertex("l"), g.get_vertex("i")))
    g.add_edges(Edge(g.get_vertex("l"), g.get_vertex("e")))
    g.add_edges(Edge(g.get_vertex("l"), g.get_vertex("s")))
    g.add_edges(Edge(g.get_vertex("v"), g.get_vertex("i")))
    g.add_edges(Edge(g.get_vertex("i"), g.get_vertex("a")))

    print(f"Result: {g}")

    sPath = DFS()
    path = sPath.search_path(g, g.get_vertex("l"), g.get_vertex("a"), [])

    for v in path:
        print(f"'{v.get_name()}'", end=" ")

    # El reto no es encontrar una solucion, sino encontrar la solucion mas optima.
