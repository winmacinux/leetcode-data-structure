from collections import deque


class Graph:

    def __init__(self, graph):
        if not graph:
            graph = {}
        self.graph = graph

    def getVertices(self):
        return self.graph.keys()

    def getEdges(self):

        edges = []

        for vertex in self.graph:
            for nextVertex in self.graph[vertex]:
                if {nextVertex, vertex} not in edges:
                    edges.append({vertex, nextVertex})

        return edges

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, edge):
        (vert1, vert2) = tuple(set(edge))

        if vert1 not in self.graph:
            self.graph[vert1] = [vert2]
        else:
            self.graph[vert1].append(vert2)

    # Depth first search
    def dfs(self, visited, vertex):

        if vertex not in visited:
            visited.append(vertex)
            for neighbour in self.graph[vertex]:
                self.dfs(visited, neighbour)

        return visited

    def shortestPathDFS(self, visited, org, dest):
        if dest in visited:
            return
        
        if org not in visited:
            visited.append(org)
            for neighbour in self.graph[org]:
                self.shortestPathDFS(visited, neighbour, dest)
                


    def bfs(self, visited, vertex):
        
        if vertex not in visited:
            visited.append(vertex)
            for neighbour in self.graph[vertex]:
                self.bfs(visited, neighbour)

        return visited


if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["a", "d", "c", "f"],
        "c": ["a", "d", "b"],
        "d": ["e", "b"],
        "e": ["d"],
        "f": ["b"]
    }
    g = Graph(graph)
    # g.addVertex("f")
    # print(g.getVertices())
    # g.addEdge({"f", "c"})
    # g.addEdge({"f", "b"})
    # g.addEdge({"c", "f"})
    # print(g.getEdges())

    visited = []
    g.shortestPathDFS(visited, "a", "d")
    print(visited)

    # print("DFS Traversal")
    # print(g.dfs(visited, "a"))
    # print(g.bfs(visited, "a"))
