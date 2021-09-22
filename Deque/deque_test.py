import unittest

from Deque.deque import Deque
from collections import deque


class TestQuickSort(unittest.TestCase):

    def test_push_front(self):
        my_dq = Deque()
        correct_dq = deque()

        my_dq.push_front(5)
        my_dq.push_front(-2)
        my_dq.push_front(100)
        my_dq.push_front(11512)
        my_dq.push_front(3131)

        arr = my_dq.deque_to_list()

        correct_dq.appendleft(5)
        correct_dq.appendleft(-2)
        correct_dq.appendleft(100)
        correct_dq.appendleft(11512)
        correct_dq.appendleft(3131)

        correct_arr = list(correct_dq)

        self.assertEqual(arr, correct_arr)

    def test_push_back(self):
        my_dq = Deque()
        correct_dq = deque()

        my_dq.push_back(1)
        my_dq.push_back(131)
        my_dq.push_back(13411)
        my_dq.push_back(-5)

        correct_dq.append(1)
        correct_dq.append(131)
        correct_dq.append(13411)
        correct_dq.append(-5)

        arr = my_dq.deque_to_list()
        correct_arr = list(correct_dq)
        self.assertEqual(arr, correct_arr)

    def test_pop_front(self):
        my_dq = Deque()
        correct_dq = deque()

        my_dq.push_back(1)
        my_dq.push_back(131)
        my_dq.push_back(13411)
        my_dq.push_back(-5)
        my_dq.pop_front()
        my_dq.pop_front()

        correct_dq.append(1)
        correct_dq.append(131)
        correct_dq.append(13411)
        correct_dq.append(-5)
        correct_dq.popleft()
        correct_dq.popleft()

        arr = my_dq.deque_to_list()
        correct_arr = list(correct_dq)
        self.assertEqual(arr, correct_arr)

    def test_pop_back(self):
        my_dq = Deque()
        correct_dq = deque()

        my_dq.push_back(1)
        my_dq.push_back(131)
        my_dq.push_back(13411)
        my_dq.push_back(-5)
        my_dq.pop_back()
        my_dq.pop_back()

        correct_dq.append(1)
        correct_dq.append(131)
        correct_dq.append(13411)
        correct_dq.append(-5)
        correct_dq.pop()
        correct_dq.pop()

        arr = my_dq.deque_to_list()
        correct_arr = list(correct_dq)
        self.assertEqual(arr, correct_arr)
