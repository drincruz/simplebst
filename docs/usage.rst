========
Usage
========

To use Simple Binary Search Tree in a project::

    # At minimal, you'll need to import simplebst.Node
    from simplebst import Node

    # Create a single element tree with value of 23
    # Its left and right sub-trees are set to None
    tree = Node(23)


Get the value of a Node::

    tree.get_value()


Get the left/right child Node of a Node::

    tree.get_left()
    tree.get_right()


Insert a new node into the tree::

    # Import simplebst.utils.insert_node
    from simplebst.utils import insert_node

    # Insert a node will modify the tree you specify
    # So, we'll use our previous example of "tree"
    insert_node(tree, 17)

    # If you were curious you should see the correct
    # value if you do the following
    tree.get_left().get_value()

    # Let's fill the tree with values
    for value in [18, 27, 53, 11]:
        insert_node(tree, value)


In-order traversals

    in_order_nodes generator::
       
        from simplebst.traversals import in_order_nodes

        # Use a generator to get all nodes in-order
        for node in in_order_nodes(tree):
            print(node.get_value())

        # You _should_ get the following:
        # 11
        # 17
        # 18
        # 23
        # 27
        # 53


    in_order_list::

        from simplebst.traversals import in_order_list

        # We need to store the values in a list,
        # so we'll create an empty one
        ordered_list = []

        # in_order_list will modify ordered_list with
        # Node()'s from the tree in-order
        in_order_list(tree, ordered_list)

        # You can now iterate the ordered_list
        for node in ordered_list:
            print(node.get_value())


Level-order traversals

    level_order_nodes generator::

        from simplebst.traversals import level_order_nodes

        # Use a generator to get all nodes in level-order
        for node in level_order_nodes(tree):
            print(node.get_value())

        # You _should_ get the following:
        # 23
        # 17
        # 27
        # 11
        # 18
        # 53


    level_order_list::

        from simplebst.traversals import level_order_list

        # level_order_list() returns a list
        # so we can iterate it like so
        for node in level_order_list(tree):
            print(node.get_value())

Pre-order traversals

    pre_order_nodes generator::

        from simplebst.traversals import pre_order_nodes

        # Use a generator to get all nodes in pre-order
        for node in pre_order_nodes(tree):
            print(node.get_value())

        # You _should_ get the following:
        # 23
        # 17
        # 11
        # 18
        # 27
        # 53


    pre_order_list::

        from simplebst.traversals import pre_order_list

        # We need to store the values in a list,
        # so we'll create an empty one
        pre_ordered_list = []

        # pre_order_list will modify pre_ordered_list with
        # Node()'s from the tree in pre-order
        pre_order_list(tree, pre_ordered_list)

        # You can now iterate the ordered_list
        for node in pre_ordered_list:
            print(node.get_value())

Post-order traversals

    post_order_nodes generator::

        from simplebst.traversals import post_order_nodes

        # Use a generator to get all nodes in post-order
        for node in post_order_nodes(tree):
            print(node.get_value())

        # You _should_ get the following:
        # 11
        # 18
        # 17
        # 53
        # 27
        # 23


    post_order_list::

        from simplebst.traversals import post_order_list

        # We need to store the values in a list,
        # so we'll create an empty one
        post_ordered_list = []

        # post_order_list will modify post_ordered_list with
        # Node()'s from the tree in post-order
        post_order_list(tree, post_ordered_list)

        # You can now iterate the ordered_list
        for node in post_ordered_list:
            print(node.get_value())

Useful utility functions

    tree_height::

        from simplebst.utils import tree_height

        # Get the height of the tree we've been using
        height = tree_height(tree)
        print(height)

        # You should get 2
