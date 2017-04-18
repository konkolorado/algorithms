#python3.6

from simple_tree import *

"""
Contains code to solve a special case of the independent set problem
in trees.

The independent set problem is the problem of maximizing a subset of vertices
such that no two vertices in the subset are adjacent.
This is a well known NP problem, however, in this special case it
is solvable.
"""

def independent_set(tree):
    """
    Algorithm works with any tree structure that provides basic functionality
    such as:
        get_size
        get_parent
        get_leaves
        remove_node
    """
    solution = []
    while tree.get_size() != 0:
        leaves = tree.get_leaves()
        solution += leaves
        parents = set([])
        for leaf in leaves:
            tree.remove_node(leaf)
            parents.add(tree.get_parent(leaf))

        for parent in parents:
            tree.remove_node(parent)

    return solution

def independent_set_max_weight(tree):
    """
    Algorithm finds a maximum vertex cover where each vertex is weighted.
    Returns the maximized weighting
    """
    solution = []
    all_nodes = tree.get_nodes()
    weighted_subtrees = { node:float('inf') for node in all_nodes }
    top = tree.get_children(tree.get_root())[0]
    return independent_set_max_weight_helper(tree, weighted_subtrees,top)

def independent_set_max_weight_helper(tree, weighted_subtrees, node):
    if weighted_subtrees[node] == float('inf'):
        if len(tree.get_children(node)) == 0:
            weighted_subtrees[node] = node.value
        else:
            m1 = node.value
            for child in tree.get_children(node):
                for g_child in tree.get_children(child):
                    m1 += independent_set_max_weight_helper(tree, weighted_subtrees, g_child)
            m0 = 0
            for child in tree.get_children(node):
                m0 += independent_set_max_weight_helper(tree, weighted_subtrees, child)

            weighted_subtrees[node] = max(m0, m1)

    return weighted_subtrees[node]
