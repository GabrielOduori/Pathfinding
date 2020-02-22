"""
This is what adds complexity to graph search, because we’re going to start 
processing locations in a better order than “first in, first out”.
What do we need to change?

1. The graph needs to know cost of movement.
2. The queue needs to return nodes in a different order.
3. The search needs to keep track of these costs from the graph and give them to the queue.

"""

import heapq


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