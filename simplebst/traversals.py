"""
BST Traversals

"""

def in_order_nodes(root):
    """
    In-order traversal of tree
    that returns a generator object

    Keyword arguments:
    root - The root of the tree to traverse
    """
    if root.get_left():
        for node in in_order_nodes(root.get_left()):
            yield node

    yield root

    if root.get_right():
        for node in in_order_nodes(root.get_right()):
            yield node

def in_order_list(root, lst):
    """
    In-order traversal of tree
    that returns a list

    Keyword arguments:
    root - The root of the tree to traverse
    """
    if None is root:
        return
    in_order_list(root.get_left(), lst)
    lst.append(root)
    in_order_list(root.get_right(), lst)

def post_order_nodes(root):
    """
    Post-order traversal of tree
    that returns a generator object

    Keyword arguments:
    root - The root of the tree to traverse
    """
    if root.get_left():
        for node in in_order_nodes(root.get_left()):
            yield node

    if root.get_right():
        for node in in_order_nodes(root.get_right()):
            yield node

    yield root

def post_order_list(root, lst):
    """
    Post-order traversal of tree
    that returns a list

    Keyword arguments:
    root - The root of the tree to traverse
    """
    if None is root:
        return
    post_order_list(root.get_left(), lst)
    post_order_list(root.get_right(), lst)
    lst.append(root)
