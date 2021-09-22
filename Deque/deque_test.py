import unittest

from Deque.deque import Deque


class TestQuickSort(unittest.TestCase):

    def test_push_front(self):
        actual_value = Deque()

        actual_value.push_front(5)
        actual_value.push_front(-2)
        actual_value.push_front(100)
        actual_value.push_front(11512)
        actual_value.push_front(3131)

        arr = actual_value.to_list()

        correct_arr = [3131, 11512, 100, -2, 5]

        self.assertEqual(arr, correct_arr)

    def test_push_back(self):
        actual_value = Deque()

        actual_value.push_back(1)
        actual_value.push_back(131)
        actual_value.push_back(13411)
        actual_value.push_back(-5)

        arr = actual_value.to_list()

        correct_arr = [1, 131, 13411, -5]
        self.assertEqual(arr, correct_arr)

    def test_pop_front(self):
        actual_value = Deque()

        actual_value.push_back(1)
        actual_value.push_back(131)
        actual_value.push_back(13411)
        actual_value.push_back(-5)
        actual_value.pop_front()
        actual_value.pop_front()

        arr = actual_value.to_list()

        correct_arr = [13411, -5]

        self.assertEqual(arr, correct_arr)

    def test_pop_back(self):
        actual_value = Deque()

        actual_value.push_back(1)
        actual_value.push_back(131)
        actual_value.push_back(13411)
        actual_value.push_back(-5)
        actual_value.pop_back()
        actual_value.pop_back()

        arr = actual_value.to_list()
        correct_arr = [1, 131]
        self.assertEqual(arr, correct_arr)

    def test_get_front(self):
        actual_value = Deque()

        actual_value.push_front(5)
        actual_value.push_front(-2)
        actual_value.push_front(100)
        actual_value.push_front(11512)
        actual_value.push_front(3131)

        arr = actual_value.to_list()

        correct_arr = [3131, 11512, 100, -2, 5]

        self.assertEqual(actual_value.get_front(), correct_arr[0])
        self.assertEqual(arr, correct_arr)
