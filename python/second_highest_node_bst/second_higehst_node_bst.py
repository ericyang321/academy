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


def traverse_to_right_most_node(node):
    ref = node
    while ref.right:
        ref = ref.right

    return ref


def second_largest_in_bst(root_node):
    if is_leaf(root_node):
        raise TypeError("There needs to be more than 1 node")

    if root_node.right is None:
        return traverse_to_right_most_node(root_node.left)

    node = root_node

    while node:
        if node.right is None:
            return traverse_to_right_most_node(node.left)

        if is_leaf(node.right):
            return node

        node = node.right
