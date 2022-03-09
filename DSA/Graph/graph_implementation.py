
class Graph:
    def __init__(self, graph=None):
        if graph is None:
            graph = {}
        self.graph = graph
        print(self.graph)

    def addVertex(self, vertex, edge):
        self.graph[vertex].append(edge)

    def breadthFirstSearch(self, vertex):
        queue = [vertex]
        visited = [vertex]

        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for i in self.graph[deVertex]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

    def depthFirstSearch(self, vertex):
        stack = [vertex]
        visited = [vertex]

        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for i in self.graph[popVertex]:
                if i not in visited:
                    stack.append(i)
                    visited.append(i)




customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "g"],
    "c": ["d", "e"],
    "d": ["b", "c", "f"],
    "e": ["c", "f"],
    "f": ["e", "d", "g"],
    "g": ["b", "f"]
}

graph = Graph(customDict)
# graph.breadthFirstSearch('a')
# print('DFS')
graph.depthFirstSearch('a')
