import random
from unittest import TestCase
from measures_of_variability import *
import statistics


class TestRange(TestCase):
    def test_get_range(self):
        self.test_list = [1, 2, 3, 4, 5]

        res = get_range(self.test_list)
        expected = 4

        self.assertEqual(expected, res)


class TestVarianceValues(TestCase):
    def test_get_variance_1(self):
        self.test_list = [1, 2, 3, 4, 5]

        res = get_variance(self.test_list)
        expected = statistics.variance(self.test_list)

        self.assertEqual(expected, res)

    def test_get_variance_2(self):
        self.test_list = [random.randint(1, 100) for _ in range(random.randint(50, 100))]

        res = round(get_variance(self.test_list), 5)
        expected = round(statistics.variance(self.test_list), 5)

        self.assertEqual(expected, res)


class TestStdDevValues(TestCase):
    def test_get_standart_deviation(self):
        self.test_list = [1, 2, 3, 4, 5]

        res = get_standart_deviation(self.test_list)
        expected = statistics.stdev(self.test_list)

        self.assertEqual(expected, res)
