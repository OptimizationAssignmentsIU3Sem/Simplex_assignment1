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

    def testCase4(self):
        correct_X = [2, 2, 0, 0]
        correct_Z = 10
        z_f = np.array([3, 2, 0, 0])
        cond = np.array([
            [1, 1, 1, 0],
            [2, 1, 0, 1]
        ])
        b_col = np.array([4, 6])
        # Assertions
        ans = simplex(z_f, cond, b_col)
        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z)
        [self.assertAlmostEqual(entry, correct_X[idx])
         for idx, entry in enumerate(ans)]

    def testCase5(self):
        z_f = np.array([4, 1, 0, 0])  # Coefficients of the objective function
        cond = np.array([
            [1, 2, 1, 0],   # Coefficients for x + 2y ≤ 6
            [2, 3, 0, 1]    # Coefficients for 2x + 3y ≤ 12
        ])
        b_col = np.array([6, 12])  # Right-hand side values for constraints

        ans = simplex(z_f, cond, b_col)

        correct_X = [6, 0, 0, 0]
        correct_Z = 24

        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z)
        [self.assertAlmostEqual(entry, correct_X[idx])
         for idx, entry in enumerate(ans)]

    def testCase6(self):
        z_f = np.array([2, 3, 0, 0])  # Coefficients of the objective function
        cond = np.array([
            [1, 3, 1, 0],   # Coefficients for x + 3y ≤ 9
            [3, 2, 0, 1]    # Coefficients for 3x + 2y ≤ 12
        ])
        b_col = np.array([9, 12])  # Right-hand side values for constraints

        # Call
        ans = simplex(z_f, cond, b_col)

        correct_X = [2.57, 2.14, 0, 0]
        correct_Z = 11.57

        # Assert
        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z, places=2)
        [self.assertAlmostEqual(entry, correct_X[idx], places=2)
         for idx, entry in enumerate(ans)]

    def testCase7(self):
        z_f = np.array([3, 1, 0, 0])  # Coefficients of the objective function
        cond = np.array([
            [2, 2, 1, 0],   # Coefficients for 2x + 2y ≤ 10
            [1, 1, 0, 1]    # Coefficients for x + y ≤ 6
        ])
        b_col = np.array([10, 6])

        ans = simplex(z_f, cond, b_col)

        correct_X = [5, 0, 0, 1]
        correct_Z = 15

        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z, places=2)
        [self.assertAlmostEqual(entry, correct_X[idx], places=2)
         for idx, entry in enumerate(ans)]

    def testCase8(self):
        # Coefficients of the objective function
        z_f = np.array([1, 2, 3, 4, 0, 0, 0, 0])
        cond = np.array([
            [1, 1, 1, 1, 1, 0, 0, 0],   # Coefficients for x1 + x2 + x3 + x4 ≤ 40
            # Coefficients for 2x1 + x2 + x3 + 3x4 ≤ 50
            [2, 1, 1, 3, 0, 1, 0, 0],
            # Coefficients for x1 + x2 + 2x3 + 2x4 ≤ 45
            [1, 1, 2, 2, 0, 0, 1, 0],
        ])
        b_col = np.array([40, 50, 45])

        #
        ans = simplex(z_f, cond, b_col)

        correct_X = [0, 35, 0, 5, 0, 0, 0, 0]
        correct_Z = 90

        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z, places=2)
        [self.assertAlmostEqual(entry, correct_X[idx], places=2)
         for idx, entry in enumerate(ans)]

    def testCase9(self):
        # Setup
        # Coefficients of the objective function
        z_f = np.array([3, 1, 2, 1, 0, 0, 0, 0])
        cond = np.array([
            # Coefficients for x1 + 2x2 + x3 + x4 ≤ 30
            [1, 2, 1, 1, 1, 0, 0, 0],
            # Coefficients for x1 + x2 + 2x3 + 3x4 ≤ 40
            [1, 1, 2, 3, 0, 1, 0, 0],
            # Coefficients for 2x1 + x2 + x3 + x4 ≤ 35
            [2, 1, 1, 1, 0, 0, 1, 0],
        ])
        # Right-hand side values for constraints
        b_col = np.array([30, 40, 35])

        # Call
        ans = simplex(z_f, cond, b_col)

        # Illustrative solution is x1=5, x2=10, x3=5, x4=5
        correct_X = [10, 0, 15, 0, 5, 0, 0, 0]
        correct_Z = 60

        # Assert
        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z, places=2)
        [self.assertAlmostEqual(entry, correct_X[idx], places=2)
         for idx, entry in enumerate(ans)]

    def testCase10(self):
        z_f = np.array([2, 3, 1, 2, 0, 0, 0, 0])
        cond = np.array([
            [1, 1, 1, 2, 1, 0, 0, 0],
            [1, 3, 2, 1, 0, 1, 0, 0],
            [2, 2, 1, 3, 0, 0, 1, 0],
        ])
        b_col = np.array([20, 25, 30])

        ans = simplex(z_f, cond, b_col)

        correct_X = [10, 5, 0, 0, 5, 0, 0, 0]
        correct_Z = 35

        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z, places=2)
        [self.assertAlmostEqual(entry, correct_X[idx], places=2)
         for idx, entry in enumerate(ans)]

    def testCaseExtra(self):
        z_f = np.array([1, 2, 3, 4, 0, 0, 0, 0])
        cond = np.array([
            [2, 1, 1, 1, 1, 0, 0, 0],
            [1, 2, 2, 1, 0, 1, 0, 0],
            [1, 1, 3, 2, 0, 0, 1, 0],
        ])
        b_col = np.array([15, 18, 20])

        ans = simplex(z_f, cond, b_col)

        correct_X = [0, 0, 0, 10, 5, 8, 0, 0]
        correct_Z = 40

        self.assertAlmostEqual(get_z_of_x(z_f, ans), correct_Z, places=2)
        [self.assertAlmostEqual(entry, correct_X[idx], places=2)
         for idx, entry in enumerate(ans)]


def run_tests():
    unittest.main()
