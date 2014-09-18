"""
Binary Search Tree

"""

import pkg_resources


class Node(object):
    """
    Data structure to represent a
    node in a BST

    """

    def __init__(self, val):
        """
        Initialize the node with a value

        Keyword arguments
        val - Value to set the node to
        """
        self._value = val
        self._left = None
        self._right = None

    def get_value(self):
        """
        Return the value of node

        """
        return self._value

    def get_left(self):
        """
        Return the left child node

        """
        return self._left

    def get_right(self):
        """
        Return the right child node

        """
        return self._right

    def set_left(self, node):
        """
        Set the left child node

        """
        self._left = node

    def set_right(self, node):
        """
        Set the right child node

        """
        self._right = node 
