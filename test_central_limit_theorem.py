from unittest import TestCase
from scipy import stats
from central_limit_theorem import *


class TestSE(TestCase):
    def test_get_se(self):
        self.test_list = [1, 2, 3, 4, 5]

        res = get_se(self.test_list)
        expected = stats.sem(self.test_list)

        self.assertEqual(expected, res)
