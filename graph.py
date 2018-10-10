# 6.0002 Problem Set 2
# Graph Optimization
# Name: Carlos Hernandez
# Collaborators: None
# Time: 40 min

import unittest

#
# A set of data structures to represent the graphs that you will be using for this pset.
#

class Node(object):
    """Represents a node in the graph"""
    def __init__(self, name):
        self.name = str(name)

    def get_name(self):
        ''' return: the name of the node '''
        return self.name

    def __str__(self):
        ''' return: The name of the node.
                This is the function that is called when print(node) is called.
        '''
        return self.name

    def __repr__(self):
        ''' return: The name of the node.
                Formal string representation of the node
        '''
        return self.name

    def __eq__(self, other):
        ''' returns: True is self == other, false otherwise
                 This is function called when you used the "==" operator on nodes
        '''
        return self.name == other.name

    def __ne__(self, other):
        ''' returns: True is self != other, false otherwise
                This is function called when you used the "!=" operator on nodes
        '''
        return not self.__eq__(other)

    def __hash__(self):
        ''' This function is necessary so that Nodes can be used as
        keys in a dictionary, even though Nodes are mutable
        '''
        return self.name.__hash__()
        
    def get_building_num(self):
        ''' returns: the integer building number '''
        return int(self.name)


## PROBLEM 1: Implement this class based on the diven docstring.
class WeightedEdge(object):
    """Represents an edge with an integer weight"""
    def __init__(self, src, dest, total_distance):
        """ Initialize  src, dest, and total_distance for the WeightedEdge class
            src: Node representing the source node
            dest: Node representing the destination node
            total_distance: int representing the distance between the src and dest
        """
        self.src = src
        self.dest = dest
        self.total_distance = total_distance
        pass #TODO
    
    def get_source(self):
        """ Getter method for WeightedEdge
            returns: Node representing the source node """
        return self.src
        pass #TODO

    def get_destination(self):
        """ Getter method for WeightedEdge
            returns: Node representing the destination node """
        return self.dest
        pass #TODO
        
    def get_total_distance(self):
        """ Getter method for WeightedEdge
            returns: int representing the distance between the source and dest nodes"""
        return self.total_distance
        pass #TODO

    def __str__(self):
        """ to string method
            returns: string with the format src->dest (total_distance)"""
        return str(self.src) + "->" + str(self.dest) + " (" + str(self.total_distance) + ")"
        pass #TODO


## PROBLEM 1: Implement methods of this class based on the diven docstring.
## DO NOT CHANGE THE FUNCTIONS THAT HAVE BEEN IMPLEMENTED FOR YOU.
class Digraph(object):
    """Represents a directed graph of Node and WeightedEdge objects"""
    def __init__(self):
        self.nodes = set([])
        self.edges = {}  # must be a dictionary of Node -> list of edges

    def __str__(self):
        edge_strs = []
        for edges in self.edges.values():
            for edge in edges:
                edge_strs.append(str(edge))
        edge_strs = sorted(edge_strs)  # sort alphabetically
        return '\n'.join(edge_strs)  # concat edge_strs with "\n"s between them

    def get_edges_for_node(self, node):
        ''' param: node object
            return: all of the edges for given node.
        '''
        return self.edges[node]
        pass #TODO

    def has_node(self, node):
        ''' param: node object
            return: True, if node is in the graph. False, otherwise.
        '''
        return node in self.edges
        pass #TODO

    def add_node(self, node):
        """ param: node object
            Adds a Node object to the Digraph.
            Raises a ValueError if it is already in the graph."""
        if node in self.edges:
            raise ValueError
        else:
            self.nodes.add(node)
            self.edges[node] = []


    def add_edge(self, edge):
        """ param: node object
            Adds an WeightedEdge instance to the Digraph.
            Raises a ValueError if either of the nodes associated with the edge is not in the  graph."""
        if edge.get_source() in self.edges and edge.get_destination() in self.edges:
            self.edges[edge.get_source()].append(edge)
        else:
            raise ValueError

