import unittest

from tarjan import Graph


class TestTarjanAlgorithm(unittest.TestCase):
    def test_tarjan_1(self):
        g1 = Graph(5)
        g1.add_vertex(1, 0)
        g1.add_vertex(0, 2)
        g1.add_vertex(2, 1)
        g1.add_vertex(0, 3)
        g1.add_vertex(3, 4)

        self.assertEqual(g1.tarjan(), [[4], [3], [1, 2, 0]])

    def test_tarjan_2(self):
        g2 = Graph(11)
        g2.add_vertex(0, 2)
        g2.add_vertex(2, 4)
        g2.add_vertex(2, 10)
        g2.add_vertex(4, 8)
        g2.add_vertex(4, 6)
        g2.add_vertex(4, 0)
        g2.add_vertex(6, 8)
        g2.add_vertex(8, 7)
        g2.add_vertex(8, 1)
        g2.add_vertex(8, 3)
        g2.add_vertex(1, 3)
        g2.add_vertex(1, 9)
        g2.add_vertex(3, 6)
        g2.add_vertex(7, 5)
        g2.add_vertex(10, 5)
        g2.add_vertex(10, 7)
        g2.add_vertex(9, 7)
        g2.add_vertex(5, 9)

        self.assertEqual(g2.tarjan(), [[9, 5, 7], [6, 3, 1, 8], [10], [4, 2, 0]])

    def test_tarjan_3(self):
        g3 = Graph(7)
        g3.add_vertex(0, 1)
        g3.add_vertex(0, 3)
        g3.add_vertex(1, 2)
        g3.add_vertex(2, 0)
        g3.add_vertex(3, 1)
        g3.add_vertex(3, 4)
        g3.add_vertex(4, 5)
        g3.add_vertex(4, 6)
        g3.add_vertex(6, 5)

        self.assertEqual(g3.tarjan(), [[5], [6], [4], [3, 2, 1, 0]])

    def test_tarjan_4(self):
        g4 = Graph(11)
        g4.add_vertex(0, 1)
        g4.add_vertex(0, 3)
        g4.add_vertex(1, 2)
        g4.add_vertex(1, 4)
        g4.add_vertex(2, 0)
        g4.add_vertex(2, 6)
        g4.add_vertex(3, 2)
        g4.add_vertex(4, 5)
        g4.add_vertex(4, 6)
        g4.add_vertex(5, 6)
        g4.add_vertex(5, 7)
        g4.add_vertex(5, 8)
        g4.add_vertex(5, 9)
        g4.add_vertex(6, 4)
        g4.add_vertex(7, 9)
        g4.add_vertex(8, 9)
        g4.add_vertex(9, 8)

        self.assertEqual(g4.tarjan(), [[8, 9], [7], [5, 4, 6], [3, 2, 1, 0], [10]])
