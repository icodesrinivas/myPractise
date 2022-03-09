"""
1. Set A cost to 0 and other vertex cost to infinity
2. If we start from A, then the formula to calculate cost of adjacent vertex will be,
        cost of adjVertex = cost of A + edge weight
3. cost of all adjVertex is calculated for A.
4. After calculating the cost of adjVertex, find the minimum cost between adjVertex
5. The next source vertex to move for shortest path should be the minimum adjVertex cost.
"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode) #
        self.distances[(fromNode, toNode)] = distance



def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:

        minNode = None

        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break
        # minNode decision ends here
        # Find the path of the edges if minNode
        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path


customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)
# print('nodes', customGraph.nodes)
# print('edges', customGraph.edges)
# print('distances', customGraph.distances)
print(customGraph.nodes)
print(customGraph.distances)
print(dijkstra(customGraph, "A"))

# See change the distance from d to e to 1 and from b to e to 6.
# then to get to e from a ,
# shortest path should be a b d e
# but your code is giving a b e