"""
Binary Search Tree

"""

class Node(object):
    """
    Binary Search Tree Node

    """

    def __init__(self, val):
        self._value = val
        self._left = None
        self._right = None

    def getValue(self):
        return self._value

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setLeft(self, node):
        self._left = node

    def setRight(self, node):
        self._right = node 


## Functions to assist with creating a BST
def insert_node(root, val):
    """
    Inserts a new node into a binary search tree

    """
    if val < root.getValue():
        if not root.getLeft():
            return root.setLeft(Node(val))
        else:
            return insert_node(root.getLeft(), val)
    elif val > root.getValue():
        if not root.getRight():
            return root.setRight(Node(val))
        else:
            return insert_node(root.getRight(), val)

def print_tree(root):
    print(root.getValue())
