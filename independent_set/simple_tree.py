#python3.6

"""
An implementation of a very simple tree datastructure
"""
class Node(object):
    def __init__(self, depth, parent, _id, value):
        self.depth = depth
        self.parent = parent
        self.children = []
        self.id = _id
        self.value = value

    def __str__(self):
        if self.value == None:
            return str(self.id)
        return str(self.value)

class SimpleTree(object):
    def __init__(self):
        self.max_id = 0
        self.size = 0
        self.root = Node(0, None, self.max_id, None)

    def __str__(self):
        inner_nodes = [self.root]
        s = ""
        while len(inner_nodes) != 0:
            curr = inner_nodes.pop()
            s += str(curr) + " "
            inner_nodes += self.get_children(curr)
        return s

    def add_child(self, node, value=None):
        depth = node.depth + 1
        new_node = Node(depth, node, self.max_id + 1, value)
        node.children.append(new_node)
        self.size += 1
        self.max_id += 1
        return new_node

    def add_child_to_node(self, node, new_child):
        node.children.append(new_child)

    def get_size(self):
        return self.size

    def get_root(self):
        return self.root

    def get_parent(self, node):
        return node.parent

    def set_parent(self, node, new_parent):
        node.parent = new_parent

    def get_child(self, node):
        if len(node.children) > 0:
            return node.children[0]
        return None

    def get_children(self, node):
        return node.children

    def get_leaves(self):
        children, leaves = [self.root], []
        while len(children) != 0:
            curr = children.pop()
            if len(curr.children) == 0:
                leaves.append(curr)
            else:
                children += self.get_children(curr)
        return leaves

    def remove_node(self, node):
        if node == self.get_root():
            return

        parent = self.get_parent(node)
        children  = self.get_children(node)

        self.get_children(parent).remove(node)
        for child in children:
            self.add_child_to_node(parent, child)

        for child in children:
            self.set_parent(child, parent)

        self.size -= 1

    def get_nodes(self):
        all_nodes = []
        to_explore = [self.root]
        while len(to_explore) != 0:
            curr = to_explore.pop()
            all_nodes.append(curr)
            to_explore += self.get_children(curr)
        return all_nodes
