===============================
Simple Binary Search Tree
===============================

.. image:: https://badge.fury.io/py/simplebst.png
    :target: http://badge.fury.io/py/simplebst

.. image:: https://travis-ci.org/drincruz/simplebst.png?branch=master
        :target: https://travis-ci.org/drincruz/simplebst

.. image:: https://pypip.in/d/simplebst/badge.png
        :target: https://pypi.python.org/pypi/simplebst


Simple Binary Search Tree is a simple implementation of a binary search tree

* Free software: MIT license
* Documentation: https://simplebst.readthedocs.org.

Features
--------

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


    For more detailed usage, please see the usage documentation: https://simplebst.readthedocs.org/en/latest/usage.html
