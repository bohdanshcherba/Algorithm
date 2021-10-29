import unittest
from dfs import *


class TestDfs(unittest.TestCase):

    def test_dfs_1(self):
        res = [160, 122, 9, 139, 134, 93, 143, 190, 107, 44, 121, 65, 132, 109, 140, 132, 24, 186, 80, 31, 169, 40, 198]

        self.assertEqual(deap_first_search('graph1.txt'), res)

    def test_dfs_2(self):
        res = False

        self.assertEqual(deap_first_search('graph2.txt'), res)

    def test_dfs_3(self):
        res = [0, 10, 5]

        self.assertEqual(deap_first_search('graph3.txt'), res)