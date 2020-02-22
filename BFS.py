"""
#
Implementing Breadth First Search in Python.
These are the abstractions we will use:

Graph:a data structure that can tell me the neighbors for each graph location. A weighted graph can also tell me the cost of moving along an edge.

Locations:A simple value (int, string, tuple, etc.) that labels locations in the graph. These are not necessarily locations on the map. They may include additional 
information such as direction, fuel, lane, or inventory, depending on the problem being solved.

Search: An algorithm that takes a graph, a starting graph location, and optionally a goal graph location, and calculates some useful information (visited, parent pointer, 
distance) for some or all graph locations.

Queue: Data structure used by the search algorithm to decide the order in which to process the graph locations.
"""
import collections

class SimpleGraph():
    def __init__(self):
        self.edges = {}

    
    def neighbors(self, id):
        return self.edges[id]

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements)==0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()
        


example_graph = SimpleGraph()
example_graph.edges = {
    
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}