"""
A* Search#
Both Greedy Best-First Search and A* use a heuristic function. 
The only difference is that A* uses both the heuristic and the ordering from Dijkstra’s Algorithm. 

"""

class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id):
        return self.edges[id]


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]



def heuristic(a,b):
    (x1,y1) = a
    (x2,y2) = b

    return abs(x1 - x2) + abs(y1 - y2)



