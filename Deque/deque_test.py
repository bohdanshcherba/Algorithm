import unittest

from Deque.deque import Deque


class TestQuickSort(unittest.TestCase):

    def test_push_front(self):
        my_dq = Deque()

        my_dq.push_front(5)
        my_dq.push_front(-2)
        my_dq.push_front(100)
        my_dq.push_front(11512)
        my_dq.push_front(3131)

        arr = my_dq.to_list()

        correct_arr = [3131, 11512, 100, -2, 5]

        self.assertEqual(arr, correct_arr)

    def test_push_back(self):
        my_dq = Deque()

        my_dq.push_back(1)
        my_dq.push_back(131)
        my_dq.push_back(13411)
        my_dq.push_back(-5)

        arr = my_dq.to_list()

        correct_arr = [1, 131, 13411, -5]
        self.assertEqual(arr, correct_arr)

    def test_pop_front(self):
        my_dq = Deque()

        my_dq.push_back(1)
        my_dq.push_back(131)
        my_dq.push_back(13411)
        my_dq.push_back(-5)
        my_dq.pop_front()
        my_dq.pop_front()

        arr = my_dq.to_list()

        correct_arr = [13411, -5]

        self.assertEqual(arr, correct_arr)

    def test_pop_back(self):
        actionaly_dq = Deque()

        actionaly_dq.push_back(1)
        actionaly_dq.push_back(131)
        actionaly_dq.push_back(13411)
        actionaly_dq.push_back(-5)
        actionaly_dq.pop_back()
        actionaly_dq.pop_back()

        arr = actionaly_dq.to_list()
        correct_arr = [1, 131]
        self.assertEqual(arr, correct_arr)
