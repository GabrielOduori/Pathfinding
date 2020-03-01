"""
#
Implementing Breadth First Search in Python.
These are the abstractions used:

Graph:a data structure that can tell me the neighbors for each graph location. A weighted graph can
also tell me the cost of moving along an edge.

Locations:A simple value (int, string, tuple, etc.) that labels locations in the graph. These are 
not necessarily locations on the map. They may include additional information such as direction, 
fuel, lane, or inventory, depending on the problem being solved.

Search: An algorithm that takes a graph, a starting graph location, and optionally a goal graph 
location, and calculates some useful information (visited, parent pointer, distance) for some or
all graph locations.

Queue: Data structure used by the search algorithm to decide the order in which to process the 
graph locations.
"""
import collections
from implementation import *

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


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results



def breadth_first_search(graph, start):
    """
    Implementing BSF and priting out what we find
    """
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True


    while not frontier.empty():
        current =  frontier.get()
        print("Visiting %r" %current)
        if next not in visited:
            frontier.put(next)
            visited[next]= True


def breadth_first_search_2(graph, start):
    # return "came_from"
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    
    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    return came_from



breadth_first_search(example_graph, 'B')

example_graph = SimpleGraph()
example_graph.edges = {
    
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}



g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS # long list, [(21, 0), (21, 2), ...]
draw_grid(g)


parents = breadth_first_search_2(g, (8, 7))
draw_grid(g, width=2, point_to=parents, start=(8, 7))