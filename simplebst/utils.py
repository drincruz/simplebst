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
