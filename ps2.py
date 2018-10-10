# 6.0002 Problem Set 5
# Graph optimization
# Name: Carlos Hernandez
# Collaborators: None
# Time:

#
# Finding shortest paths through MIT buildings
#
import copy
import unittest
from graph import Digraph, Node, WeightedEdge

#
# PROBLEM 2: Building up the Campus Map
#
# PROBLEM 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# ANSWER: buildings, paths, in the weight of the edges
#


# PROBLEM 2b: Implementing load_map
def load_map(map_filename):
    """
           Parses the map file and constructs a directed graph

           Parameters:
               map_filename : name of the map file

           Assumes:
               Each entry in the map file consists of the following four positive
               integers, separated by a blank space:
                   From To TotalDistance
               e.g.
                   32 76 54
               This entry would become an edge from 32 to 76.

           Returns:
               a directed graph representing the map
           """
    print("Loading map from file...")
    with open(map_filename) as file:
        graph = Digraph()
        for line in file:
            # take out the \n from each line in the file
            line = line[:-1]

            # elements represents a list containing [source, destination, distance]
            elements = line.split(" ")
            node = Node(elements[0])
            dest = Node(elements[1])
            edge = WeightedEdge(Node(elements[0]), Node(elements[1]), int(elements[2]))

            # add the source and destination nodes to the graph if they are not already there and once they are,
            # add the edge
            if not graph.has_node(node):
                graph.add_node(node)
            if not graph.has_node(dest):
                graph.add_node(dest)
            if graph.has_node(node) and graph.has_node(dest):
                graph.add_edge(edge)
        return graph

# PROBLEM 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out

#print(load_map("test_load_map.txt"))

#
# PROBLEM 3: Finding the Shorest Path using Optimized Search Method
#
# PROBLEM 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# ANSWER: The objective function is whatever you are trying to optimize, so in this case the distance, and the constraint is the max amount of buildings.
#

# PROBLEM 3b: Implement add_node_to_path
def add_node_to_path(node, path):
    """
    Adds the name of the node to the copy of the list of strings inside the 
    safely copied version of the path. 
    Leave the other two items in path unchanged (total distance traveled and 
    total number of buildings).
    
    Parameters:
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            number of buildings.
        node: Node 
            Representing a building being added to the path
            
    Returns:
        A safely copied version of path with the node name added to the end of 
        the first element.
    """
    # need a deepcopy so that the list inside of the the list 'path' is also copied
    new_path = copy.deepcopy(path)
    new_path[0].append(node.get_name())
    return new_path

# PROBLEM 3c: Implement get_best_path
def get_best_path(digraph, start, end, path, max_buildings, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: instance of Digraph or one of its subclasses
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            number of buildings.
        max_buildings: int
            Maximum number of buildings a path can visit
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple of the form (best_dist, best_path).
        The first item is an integer, the length (distance traveled)
        of the best path.
        The second item is the shortest-path from start to end, represented by
        a list of building numbers (in strings).

        If there exists no path that satisfies max_total_dist and
        max_buildings constraints, then best_path is None.
    """
    # if the path reached the end, return the distance and the path
    if start == end:
        return path[1], path[0]

    # check all the edges of the node you are on (start)
    for edge in digraph.get_edges_for_node(Node(start)):

        # as long as we don't have a cycle
        if edge.get_destination().get_name() not in path[0]:

            # as long as we can add the destination node to the path w/o going over the building limit
            if path[2] + 1 <= max_buildings:

                # as long as adding the distance from start to destination to the path doesn't exceed the shortest distance already found
                if path[1] + edge.get_total_distance() <= best_dist:

                    # make a copy of path and add the destination node to it so that you don't mutate the path that was
                    # left behind in the rest of the destinations we still have to iterate through
                    new_path = add_node_to_path(edge.get_destination(), path)
                    new_path[1] += edge.get_total_distance()
                    new_path[2] += 1
                    dist, b_path = get_best_path(digraph, edge.get_destination().get_name(), end, new_path, max_buildings, best_dist, best_path)
                    best_dist = dist
                    best_path = b_path
    return best_dist, best_path

### USED FOR TESTING. PLEASE DO NOT CHANGE THIS FUNCTION.
def directed_dfs(digraph, start, end, max_total_dist, max_buildings):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the number of buildings on this path must
    not exceed max_buildings.

    Parameters:
        digraph: instance of Digraph or one of its subclasses
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_buildings: int
            Maximum number of buildingss a path can visit

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings).

        If there exists no path that satisfies max_total_dist and
        max_buildings constraints, then raises a ValueError.
    """
    best_path = None
    path = [[start], 0, 1]  # begin at start node with 0 distance
    best_dist, best_path = get_best_path(digraph, start, end, path,
                                         max_buildings, max_total_dist,
                                         best_path)
    if best_path is None:
        raise ValueError("No path from {} to {}".format(start, end))
    return best_path


