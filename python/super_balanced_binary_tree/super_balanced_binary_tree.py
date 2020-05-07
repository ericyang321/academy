from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = Node(value)
        return self.left

    def insert_right(self, value):
        self.right = Node(value)
        return self.right


def is_leaf(node):
    return node.left is None and node.right is None


def is_super_balanced(root_node):
    """
    A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.
    """

    if is_leaf(root_node):
        return True

    stack = deque()

    stack.append((0, root_node))
    deepest_level = 0

    while len(stack) > 0:
        level, node = stack.pop()

        if is_leaf(node):
            if abs(level - deepest_level) > 1:
                return False

            if deepest_level < level:
                deepest_level = level

        if node.left is not None:
            stack.append((level + 1, node.left))

        if node.right is not None:
            stack.append((level + 1, node.right))

    return True
