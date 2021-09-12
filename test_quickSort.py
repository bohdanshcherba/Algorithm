import unittest

from QuickSort.QuickSort_2_0 import quick_sort


class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        arr_for_sort = [3, 2, 90, 12]
        self.assertEqual(quick_sort(arr_for_sort, 0, len(arr_for_sort) - 1, 'asc'), [2, 3, 12, 90])
        arr_for_sort = [3, 2, 4, 5, 12, 41, 3, 4, -6, 120, 90, 12]

        self.assertEqual(quick_sort(arr_for_sort, 0, len(arr_for_sort) - 1, 'asc'),
                         [-6, 2, 3, 3, 4, 4, 5, 12, 12, 41, 90, 120])

        arr_for_sort = [3, 2, 90, 12, 21, -99, 13000, 213441, 212300, 9429402]

        self.assertEqual(quick_sort(arr_for_sort, 0, len(arr_for_sort) - 1, 'asc'),
                         [-99, 2, 3, 12, 21, 90, 13000, 212300, 213441, 9429402])

    def test_quick_sort_asc(self):
        arr_for_sort = [3, 2, 100, 1]

        self.assertEqual(quick_sort(arr_for_sort, 0, len(arr_for_sort) - 1, 'asc'), [1, 2, 3, 100])
        arr_for_sort = [1, 2, 3, 4]

        self.assertEqual(quick_sort(arr_for_sort, 0, len(arr_for_sort) - 1, 'asc'), [1, 2, 3, 4])

    def test_quick_sort_desc(self):
        arr_for_sort = [122, 30, 400, 112]

        self.assertEqual(quick_sort(arr_for_sort, 0, len(arr_for_sort) - 1, 'desc'), [400, 122, 112, 30])
        arr_for_sort = [400, 122, 112, 30]

        self.assertEqual(quick_sort(arr_for_sort, 0, len(arr_for_sort) - 1, 'desc'), [400, 122, 112, 30])
