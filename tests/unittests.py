import unittest
import numpy as np
from simplex import simplex, get_z_of_x


class SimplexTestCase(unittest.TestCase):
    def testCase1(self):  # test method names begin with 'test'
        # ___________(data)______________ #

        correct_X = [0, 8, 20, 0, 0, 96]
        correct_Z = 400
        z_f = np.array([9, 10, 16, 0, 0, 0])
        cond = np.array([
            [18, 15, 12, 1, 0, 0],
            [6,  4,  8,  0, 1, 0],
            [5,  3,  3,  0, 0, 1]
        ])
        b_col = np.array([360, 192, 180])

        # ------------(assertion)---------#
        ans = simplex(z_f, cond, b_col)
        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z)
        [self.assertAlmostEqual(entry, correct_X[idx]) for idx, entry in enumerate(ans)]

    def testCase2(self):
        # ___________(data)______________ #

        correct_X = [23, 4, 0, 1, 0, 0]
        correct_Z = 39

        z_f = np.array([0, 8, 0, 7, 0, 1])
        cond = np.array([
            [1, -2, 0, -3,  0, -2],
            [0,  4, 1, -4,  0, -3],
            [0,  5, 0,  5,  1,  1]
        ])
        b_col = np.array([12, 12, 25])
        # ------------(assertion)---------#

        ans = simplex(z_f, cond, b_col)
        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z)
        [self.assertAlmostEqual(entry, correct_X[idx]) for idx, entry in enumerate(ans)]

    def testCase3(self):
        # ___________(data)______________ #

        correct_X = [10/11, 72/11, 0, 0, 0, 456/11]
        correct_Z = 226/11

        z_f = np.array([1, 3, 0, -5, 0, 0])
        cond = np.array([
            [2,  4, 1, 2,  0, 0],
            [-3,  5, 0, -3,  1, 0],
            [4,  -2, 0,  8,  0,  1]
        ])
        b_col = np.array([28, 30, 32])
        # ------------(assertion)---------#

        ans = simplex(z_f, cond, b_col)
        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z)
        [self.assertAlmostEqual(entry, correct_X[idx]) for idx, entry in enumerate(ans)]


def run_tests():
    unittest.main()
