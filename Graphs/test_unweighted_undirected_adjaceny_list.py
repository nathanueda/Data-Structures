from tkinter import E, N
from unweighted_undirected_adjaceny_list import Vertex
from unweighted_undirected_adjaceny_list import UnweightedUndirectedAdjacenyList
import unittest

class TestUnweightedUndirectedAdjacenyList(unittest.TestCase):
    """Tests for UnweightedUndirectedAdjacenyList class."""

    def test_init(self):
        """Does the adjaceny list properly initialize?"""
        test_adj_list = UnweightedUndirectedAdjacenyList()
        self.assertEqual(test_adj_list.size(), 0)
    
    def test_add_vertex(self):
        """Does the add_vertex function work properly?"""
        test_adj_list = UnweightedUndirectedAdjacenyList()
        test_adj_list.add_vertex("A")
        self.assertEqual(test_adj_list.size(), 1)

        test_adj_list.add_vertex("A")
        test_adj_list.add_vertex("N")
        test_adj_list.add_vertex("E")
        test_adj_list.add_vertex("C")
        test_adj_list.add_vertex("D")
        self.assertEqual(test_adj_list.size(), 5)

    def test_remove_vertex(self):
        """Does the remove_vertex function work properly?"""
        test_adj_list = UnweightedUndirectedAdjacenyList()
        test_adj_list.add_vertex("A")
        test_adj_list.add_vertex("N")
        test_adj_list.add_vertex("E")
        test_adj_list.add_vertex("C")
        test_adj_list.add_vertex("D")

        self.assertEqual(test_adj_list.size(), 5)
        test_adj_list.remove_vertex("A")
        self.assertEqual(test_adj_list.size(), 4)

        test_adj_list.remove_vertex("A")
        self.assertEqual(test_adj_list.size(), 4)

    def test_add_edge(self):
        """Does the add_edge function work properly?"""
        test_adj_list = UnweightedUndirectedAdjacenyList()
        test_adj_list.add_vertex("A")
        test_adj_list.add_vertex("N")
        test_adj_list.add_vertex("E")
        test_adj_list.add_vertex("C")
        test_adj_list.add_vertex("D")

        test_adj_list.add_edge("A", "N")
        self.assertEqual(test_adj_list.neighbors("A"), ["N"])
        self.assertEqual(test_adj_list.neighbors("N"), ["A"])

        test_adj_list.add_edge("N", "A")
        self.assertEqual(test_adj_list.neighbors("A"), ["N"])
        self.assertEqual(test_adj_list.neighbors("N"), ["A"])
        self.assertEqual(len(test_adj_list.neighbors("N")), 1)
        self.assertEqual(len(test_adj_list.neighbors("A")), 1)

    def test_remove_vertex_and_edge(self):
        """Does the remove_vertex function and remove_edge function work 
        properly in conjunction with one another??"""
        test_adj_list = UnweightedUndirectedAdjacenyList()
        test_adj_list.add_vertex("A")
        test_adj_list.add_vertex("N")
        test_adj_list.add_vertex("E")
        test_adj_list.add_vertex("C")
        test_adj_list.add_vertex("D")

        test_adj_list.add_edge("A", "N")
        self.assertEqual(test_adj_list.neighbors("A"), ["N"])
        self.assertEqual(test_adj_list.neighbors("N"), ["A"])

        self.assertEqual(test_adj_list.size(), 5)
        test_adj_list.remove_vertex("A")
        self.assertEqual(test_adj_list.size(), 4)
        self.assertEqual(len(test_adj_list.neighbors("N")), 0)
        self.assertEqual(test_adj_list.neighbors("N"), [])

    def test_full_example(self):
        """Do the functions all work on a more complex graph example?"""

        test_adj_list = UnweightedUndirectedAdjacenyList()
        test_adj_list.add_vertex("A")
        test_adj_list.add_vertex("N")
        test_adj_list.add_vertex("E")
        test_adj_list.add_vertex("C")
        test_adj_list.add_vertex("D")

        test_adj_list.add_edge("A", "N")
        self.assertEqual(test_adj_list.neighbors("A"), ["N"])
        self.assertEqual(test_adj_list.neighbors("N"), ["A"])
        self.assertEqual(test_adj_list.size(), 5)
        test_adj_list.add_edge("A", "E")
        test_adj_list.add_edge("A", "C")
        test_adj_list.add_edge("A", "D")
        self.assertEqual(test_adj_list.neighbors("A"), ["N", "E", "C", "D"])

        test_adj_list.add_edge("N", "C")
        test_adj_list.add_edge("N", "D")
        test_adj_list.add_edge("N", "E")

        test_adj_list.remove_vertex("N")
        self.assertEqual(test_adj_list.size(), 4)

        self.assertEqual(test_adj_list.neighbors("A"), ["E", "C", "D"])


if __name__ == '__main__':
    unittest.main()