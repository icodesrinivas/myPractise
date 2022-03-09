#   Created by Elshad Karimov
#   Copyright © 2021 AppMillers. All rights reserved.

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, startNode, endNode):
        queue = [startNode]
        visited = []
        result = False
        while queue:
            popVertex = queue.pop(0)
            visited.append(popVertex)
            if popVertex == endNode:
                result = True
                break
            if popVertex in self.gdict and len(self.gdict[popVertex]) != 0:
                for edge in self.gdict[popVertex]:
                    if edge not in visited:
                        queue.append(edge)
        print(result)
        return result

c = {
    "a": ["c", "d", "b"],
    "b": ["j"],
    "c": ["g"],
    "d": [],
    "e": ["f", "a"],
    "f": ["i"],
    "g": ["d", "h"],
    "j": [],
    "i": [],
    "j": []
}

g = Graph(c)
g.checkRoute("e", "i")