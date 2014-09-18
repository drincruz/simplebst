"""
test_traversals

Tests for `simplebst` traversals.
"""

from simplebst import Node
from simplebst.traversals import in_order_list, in_order_nodes
from simplebst.utils import insert_node


class TestSimplebstTraversals(object):

    def setUp(self):
        self.root = Node(23)
        insert_node(self.root, 57)
        insert_node(self.root, 5)
        insert_node(self.root, 13)
        insert_node(self.root, 103)

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

    def tearDown(self):
        pass
