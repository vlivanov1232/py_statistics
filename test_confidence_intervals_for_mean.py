from unittest import TestCase
import scipy.stats as sp
import numpy as np

from confidence_intervals_for_mean import get_95_interval


class TestConfidenceInterval(TestCase):
    def test_get_95_interval(self):
        self.test_list = [1, 2, 3, 4, 5, 6, 7]

        res = tuple([round(x, 3) for x in get_95_interval(self.test_list)])
        expected = tuple([round(x, 3) for x in self.prepare_python_interval()])

        self.assertTupleEqual(expected, res)

    def prepare_python_interval(self):

        mean = np.mean(self.test_list)
        se = sp.sem(self.test_list)
        return mean - sp.norm.ppf(.975)*se, mean + sp.norm.ppf(.975)*se

