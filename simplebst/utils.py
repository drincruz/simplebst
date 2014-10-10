"""
Utility functions

"""

from simplebst import Node


def insert_node(root, val):
    """
    Inserts a new node into a binary search tree

    """
    if val < root.get_value():
        if not root.get_left():
            return root.set_left(Node(val))
        else:
            return insert_node(root.get_left(), val)
    elif val > root.get_value():
        if not root.get_right():
            return root.set_right(Node(val))
        else:
            return insert_node(root.get_right(), val)


def tree_height(node):
    """
    Get the height of a tree

    :param node:
    :return:
    """
    if None is node:
        return -1
    else:
        return max(
            tree_height(node.get_left()),
            tree_height(node.get_right()) + 1)
