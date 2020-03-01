"""
This is what adds complexity to graph search, because we’re going to start 
processing locations in a better order than “first in, first out”.
What do we need to change?

1. The graph needs to know cost of movement.
2. The queue needs to return nodes in a different order.
3. The search needs to keep track of these costs from the graph and give them to the queue.

"""

import heapq
from implementation import *

class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id):
        return self.edges[id]

class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}
    
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)




class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]




def dijkstra_search(graph,start, goal):

    frontier  = PriorityQueue()
    frontier.put(start,0)
    came_from = {}
    cost_so_far = {}

    came_from[start]=None 
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()


        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current]+graph.cost(current,next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
            # if new_cost < cost_so_far.get(next, Infinity):
                cost_so_far[next]  =  new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


# Finally after searching,build the path.

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []

    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path


# Testing the code now

came_from, cost_so_far = dijkstra_search(diagram4,(1,4),(7,8))
draw_grid(diagram4,width=3, point_to=came_from, start=(1,4),goal=(7,8))
print()
draw_grid(diagram4, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))
print()
draw_grid(diagram4, width=3, path=reconstruct_path(came_from, start=(1, 4), goal=(7, 8)))