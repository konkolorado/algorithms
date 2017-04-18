#python3.6

"""
Contains test code for the independent_set algorithm
"""

from independent_set import *

def make_simple_tree():
    tree = SimpleTree()
    curr = tree.get_root()
    for i in range(10):
        tree.add_child(curr)
        curr = tree.get_child(curr)
    return tree

def tree_from_example():
    tree = SimpleTree()
    curr = tree.get_root()
    three = tree.add_child(curr, 3)
    five = tree.add_child(three, 5)
    one = tree.add_child(three, 1)
    six = tree.add_child(three, 6)
    tree.add_child(five, 2)
    tree.add_child(one, 3)
    tree.add_child(six, 2)
    seven = tree.add_child(six, 7)
    tree.add_child(seven, 1)
    tree.add_child(seven, 2)
    tree.add_child(seven, 1)
    return tree

def test_tree():
    tree = make_simple_tree()

    assert tree.get_leaves()[0].id == 10
    assert tree.get_root().id == 0
    assert tree.get_child(tree.get_root()).id == 1
    assert len(tree.get_children(tree.get_root())) == 1

    tree = tree_from_example()
    leaves = tree.get_leaves()
    truth = [1,2,1,2,3,2]
    for leaf in leaves:
        assert leaf.value in truth
        truth.remove(leaf.value)

def test_independent_set():
    tree = make_simple_tree()
    inds = independent_set(tree)
    for i in inds:
        assert i.id % 2 == 0

    tree = tree_from_example()
    answer = [1,2,1,2,3,2,3]
    inds = independent_set(tree)
    for i in inds:
        assert i.value in answer
        answer.remove(i.value)

def test_independent_set_weighted():
    tree = tree_from_example()
    assert independent_set_max_weight(tree) == 18

def main():
    test_tree()
    test_independent_set()
    test_independent_set_weighted()

if __name__ == '__main__':
    main()
