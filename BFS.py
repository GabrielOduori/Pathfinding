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
