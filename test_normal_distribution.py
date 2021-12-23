import random
from unittest import TestCase
from normal_distribution import *
from scipy import stats


class TestZStandart(TestCase):
    def test_z_score_1(self):
        self.test_list = [1, 2, 3, 4, 5]

        res = z_standart(self.test_list)
        expected = stats.zscore(self.test_list, ddof=1)

        self.assertListEqual(list(expected), res)

    def test_z_score_2(self):
        self.test_list = [random.randint(1, 100) for _ in range(random.randint(50, 100))]

        res = z_standart(self.test_list)
        expected = stats.zscore(self.test_list, ddof=1)

        self.assertListEqual(list(expected), res)

