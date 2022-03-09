#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

from collections import defaultdict


class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def helperFunction(self, v, visited, stack):
        visited.append(v)

        for k in self.graph[v]:
            if k not in visited:
                self.helperFunction(k, visited, stack)

        stack.insert(0, v)


    def topologicalSort(self):

        visited = []
        stack = []

        for i in list(self.graph):
            if i not in visited:
                self.helperFunction(i, visited, stack)

        print(stack)

customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")
print(customGraph.graph)

customGraph.topologicalSort()