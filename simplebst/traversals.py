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
        for node in post_order_nodes(root.get_left()):
            yield node

    if root.get_right():
        for node in post_order_nodes(root.get_right()):
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


def pre_order_nodes(root):
    """
    Pre-order traversal of tree
    that returns a generator object

    Keyword arguments:
    root - The root of the tree to traverse
    """
    yield root

    if root.get_left():
        for node in pre_order_nodes(root.get_left()):
            yield node

    if root.get_right():
        for node in pre_order_nodes(root.get_right()):
            yield node


def pre_order_list(root, lst):
    """
    Pre-order traversal of tree
    that builds a list

    Keyword arguments:
    root - The root of the tree to traverse
    """
    if None is root:
        return
    lst.append(root)
    pre_order_list(root.get_left(), lst)
    pre_order_list(root.get_right(), lst)


def level_order_nodes(root):
    """
    Level-order traversal of tree
    that returns a generator object

    :param root:
    :return:
    """
    queue = []
    queue.append(root)

    while 0 < len(queue):
        next_node = queue.pop(0)
        if next_node.get_left():
            queue.append(next_node.get_left())
        if next_node.get_right():
            queue.append(next_node.get_right())
        yield next_node


def level_order_list(root):
    """
    Level-order traversal of tree
    that returns a list

    :param root:
    :return:
    """
    return_list = []
    queue = []
    queue.append(root)

    while 0 < len(queue):
        next_node = queue.pop(0)
        if next_node.get_left():
            queue.append(next_node.get_left())
        if next_node.get_right():
            queue.append(next_node.get_right())
        return_list.append(next_node)

    return return_list
