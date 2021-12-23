from unittest import TestCase
import statistics
import random
import math

from central_trend_measures import *


class TestMedianValues(TestCase):
    def test_get_median_even(self):
        self.test_lst = [random.randint(0, 100) for _ in range(50)]

        res = get_median(self.test_lst)
        expected = statistics.median(self.test_lst)

        self.assertEqual(expected, res)

    def test_get_median_not_even(self):
        self.test_lst = [random.randint(0, 100) for _ in range(51)]

        res = get_median(self.test_lst)
        expected = statistics.median(self.test_lst)

        self.assertEqual(expected, res)

    def test_get_median_one_value(self):
        self.test_lst = [random.randint(0, 100) for _ in range(1)]

        res = get_median(self.test_lst)
        expected = statistics.median(self.test_lst)

        self.assertEqual(expected, res)

    def test_get_median_zero_value(self):
        self.test_lst = []

        res = get_median(self.test_lst)

        self.assertTrue(math.isnan(res))


class TestMeanValues(TestCase):
    def test_get_mean(self):
        self.test_lst = [random.randint(0, 100) for _ in range(random.randint(0, 100))]

        res = get_mean(self.test_lst)
        expected = statistics.mean(self.test_lst)

        self.assertEqual(expected, res)

    def test_get_mean_one_value(self):
        self.test_lst = [random.randint(0, 100) for _ in range(1)]

        res = get_mean(self.test_lst)
        expected = statistics.mean(self.test_lst)

        self.assertEqual(expected, res)

    def test_get_mean_zero_value(self):
        self.test_lst = []

        res = get_mean(self.test_lst)

        self.assertTrue(math.isnan(res))


class TestModeValues(TestCase):
    def test_get_mode(self):
        self.test_lst = [random.randint(0, 100) for _ in range(100)]

        res = get_mode(self.test_lst)
        expected = statistics.mode(self.test_lst)

        self.assertEqual(expected, res)

    def test_get_mod_zero_value(self):
        self.test_lst = []

        res = get_mode(self.test_lst)

        self.assertTrue(math.isnan(res))
