from app.graph import UnDiGraph, DiGraph, Edge, Vertex


class DFS:

    def search_path(self, graph: DiGraph, startV: Vertex, endV: Vertex, path):
        if path is None:
            path = []
        path.append(startV)

        if startV == endV:
            return path

        for vx in graph.get_neighbours(startV):
            if vx not in path:
                new_path = self.search_path(graph, vx, endV, path)
                if new_path is not None:
                    return new_path


class BFS:
    def search_path():
        pass
