from dotenv import load_dotenv
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self) -> None:
        self.graph = None
        self.runGraph()

    def runGraph(self):
        self.graph = nx.Graph()
        self.graph.add_nodes_from(
            ["Marie Curie", "R. Feyman", "A. Einstein", "E. Schrodinguer", "C. Sagan"]
        )

        self.graph.add_edge("Marie Curie", "A. Einstein", weight=4)
        self.graph.add_edge("Marie Curie", "E. Schrodinguer", weight=7)
        self.graph.add_edge("R. Feyman", "C. Sagan", weight=9)
        self.graph.add_edge("C. Sagan", "Marie Curie", weight=3)

        return self.graph

    def runDiGraph(self):
        self.diGraph = nx.DiGraph()
        self.diGraph.add_nodes_from(
            ["Marie Curie", "R. Feyman", "A. Einstein", "E. Schrodinguer", "C. Sagan"]
        )

        self.diGraph.add_edge("Marie Curie", "A. Einstein", weight=4)
        self.diGraph.add_edge("Marie Curie", "E. Schrodinguer", weight=7)
        self.diGraph.add_edge("R. Feyman", "C. Sagan", weight=9)
        self.diGraph.add_edge("C. Sagan", "Marie Curie", weight=3)

        return self.diGraph

    def display_line(self, graph):
        print(f"Numero de veticies: {graph.number_of_nodes()}")
        print(f"Numero de aristas: {graph.number_of_edges()}")
        print(f"Numero de Nodos: {graph.nodes}")
        print(f"Numero de Aritas: {graph.edges}")

    def display_img(self, graph):
        plt.figure(figsize=(3, 3))

        spacial = nx.spring_layout(graph, seed=10)
        weights = nx.get_edge_attributes(graph, "weight")
        nx.draw(graph, spacial, with_labels=True)
        nx.draw_networkx_edge_labels(graph, spacial, edge_labels=weights)

        plt.show()


if __name__ == "__main__":
    load_dotenv()
