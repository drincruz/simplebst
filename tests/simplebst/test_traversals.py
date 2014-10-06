"""
test_traversals

Tests for `simplebst` traversals.
"""


from simplebst import Node
from simplebst.traversals import (
    in_order_list, in_order_nodes,
    level_order_nodes, level_order_list,
    pre_order_nodes, pre_order_list,
    post_order_list, post_order_nodes)

from simplebst.utils import insert_node


class TestSimplebstTraversals(object):
    """
      23
     /  \
    5   57
     \    \
     13   103

    """

    def setUp(self):
        self.root = Node(23)
        insert_node(self.root, 57)
        insert_node(self.root, 5)
        insert_node(self.root, 13)
        insert_node(self.root, 103)

    def tearDown(self):
        pass

    def test_node_creation(self):
        assert 23 == self.root.get_value()

    def test_in_order_list(self):
        """
        Test in_order_list()
        and make sure it returns an in-order list

        """
        _expected_list = [5, 13, 23, 57, 103]
        _output_list = []
        
        # Call in_order_list to test
        in_order_list(self.root, _output_list)

        # We just want to test the values
        # so make a list from the list of objects
        _sorted_output = [x.get_value() for x in _output_list]

        assert len(_expected_list) == len(_output_list)
        assert _expected_list == _sorted_output

    def test_in_order_nodes(self):
        """
        Test in_order_nodes() generator

        """
        _expected_values = [5, 13, 23, 57, 103]

        for i, val in enumerate(in_order_nodes(self.root)):
            assert _expected_values[i] == val.get_value()

    def test_post_order_list(self):
        """
        Test post_order_list() builds a proper list

        :return:
        """
        _expected_list = [13, 5, 103, 57, 23]

        _output_list = []

        # Call post_order_list to test
        post_order_list(self.root, _output_list)

        # We just want to test the values
        # so make a list from the list of objects
        _post_order_output = [x.get_value() for x in _output_list]

        assert len(_expected_list) == len(_output_list)
        assert _expected_list == _post_order_output

    def test_post_order_nodes(self):
        """
        Test post_order_nodes() generator

        """
        _expected_values = [13, 5, 103, 57, 23]

        for i, val in enumerate(post_order_nodes(self.root)):
            assert _expected_values[i] == val.get_value()

    def test_pre_order_nodes(self):
        """
        Test pre_order_nodes() generator

        """
        _expected_values = [23, 5, 13, 57, 103]

        for i, val in enumerate(pre_order_nodes(self.root)):
            assert _expected_values[i] == val.get_value()

    def test_pre_order_list(self):
        """
        Test pre_order_list() builds a proper list

        :return:
        """
        _expected_list = [23, 5, 13, 57, 103]

        _output_list = []

        # Call pre_order_list to test
        pre_order_list(self.root, _output_list)

        # We just want to test the values
        # so make a list from the list of objects
        _pre_order_output = [x.get_value() for x in _output_list]

        assert len(_expected_list) == len(_output_list)
        assert _expected_list == _pre_order_output

    def test_level_order_nodes(self):
        """
        Test level_order_nodes() generator

        """
        _expected_values = [23, 5, 57, 13, 103]

        for i, val in enumerate(level_order_nodes(self.root)):
            assert _expected_values[i] == val.get_value()

    def test_level_order_list(self):
        """
        Test level_order_list() returns proper list

        :return:
        """
        _expected_list = [23, 5, 57, 13, 103]

        # Call level_order_list to test
        _lst = level_order_list(self.root)

        # We just want to test the values
        # so make a list from the list of objects
        _level_order_output = [x.get_value() for x in _lst]

        assert len(_expected_list) == len(_level_order_output)
        assert _expected_list == _level_order_output

