from collections import deque, namedtuple


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


def is_bst(root_node):
    if root_node is None:
        raise TypeError("There's no root node")

    if root_node.left is None and root_node.right is None:
        return True

    NodeBoundPackage = namedtuple(
        "NodeBoundPackage", ["node", "lower_bound", "upper_bound"]
    )

    stack = deque()

    if root_node.left:
        stack.append(
            NodeBoundPackage(
                node=root_node.left,
                lower_bound=-float("infinity"),
                upper_bound=root_node.value,
            )
        )

    if root_node.right:
        stack.append(
            NodeBoundPackage(
                node=root_node.right,
                lower_bound=root_node.value,
                upper_bound=float("infinity"),
            )
        )

    while len(stack) > 0:
        node_bound_pkg = stack.pop()

        node = node_bound_pkg.node
        lower_bound = node_bound_pkg.lower_bound
        upper_bound = node_bound_pkg.upper_bound

        if node.value <= lower_bound or node.value >= upper_bound:
            return False

        left_node = node.left
        right_node = node.right

        if left_node:
            new_lower_bound = node.value if node.value < lower_bound else lower_bound
            stack.append(
                NodeBoundPackage(
                    node=left_node, lower_bound=new_lower_bound, upper_bound=upper_bound
                )
            )

        if right_node:
            new_upper_bound = node.value if node.value > upper_bound else upper_bound
            stack.append(
                NodeBoundPackage(
                    node=right_node,
                    lower_bound=lower_bound,
                    upper_bound=new_upper_bound,
                )
            )

    return True
