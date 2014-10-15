"""
Unit tests for utils

"""


from simplebst import Node

from simplebst.utils import insert_node, tree_height


class TestSimplebstUtils(object):
    """
    tree0
      23
     /  \
    5   57
     \    \
     13   103

    tree1
      30

    tree2
       1
        \
         2
          \
           3
            \
             5
              \
               8
                \
                 13
    """

    def setUp(self):
        self.tree0 = Node(23)
        for v in [57, 5, 13, 103]:
            insert_node(self.tree0, v)

        self.tree1 = Node(30)

        self.tree2 = Node(1)
        for v in [2, 3, 5, 8, 13]:
            insert_node(self.tree2, v)

    def tearDown(self):
        pass

    def test_tree_height(self):
        """
        Test a random tree's height

        :return:
        """
        assert 2 == tree_height(self.tree0)

    def test_1_node_tree_height(self):
        """
        Test a single node tree (no children) height

        :return:
        """
        assert 0 == tree_height(self.tree1)

    def test_one_sided_tree(self):
        """
        Test a one-sided tree
        (basically a linked list)

        :return:
        """
        assert 5 == tree_height(self.tree2)

    def test_insert_node_lt(self):
        """
        Test insert_node inserts a less-than node to the
        left child

        :return:
        """
        tmp_tree = Node(10)
        insert_node(tmp_tree, 5)
        assert 5 == tmp_tree.get_left().get_value()

    def test_insert_node_gt(self):
        """
        Test insert_node inserts a greater-than node to the
        right child

        :return:
        """
        tmp_tree = Node(10)
        insert_node(tmp_tree, 15)
        assert 15 == tmp_tree.get_right().get_value()
