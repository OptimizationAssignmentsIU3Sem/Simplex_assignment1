from typing import List

import numpy as np


def choose_basic(constr: np.array) -> List:
    basics = [0 for _ in range(len(constr))]
    for pivot in range(len(constr)):
        for column in range(len(constr[0])):
            col = constr[:, column]
            if col[pivot] == 1 and all([i == 0 for i in np.concatenate([col[:pivot], col[pivot+1:]])]):
                basics[pivot] = column
    return basics


def get_nonbasic(basic: List, n: int):
    return list(set(range(n)) - set(basic))


def simplex(z: np.array, constr: np.array, b: np.array) -> np.array:
    """method for maximization of z-function subject to given constrains."""

    basic = choose_basic(constr)
    non_basic = get_nonbasic(basic, len(constr[0]))

    improvement = True
    z_prev = []
    while improvement:  # z_r=C_bi * B_i^-1 * (P_i .. P_i, where i are non-basic) - (c_i .. c_i, where i are non-basic)

        C_b = np.array([z[i] for i in basic])
        B_i = np.array([constr[:, i] for i in basic])
        B_i = np.transpose(B_i)
        P = np.array([constr[:, i] for i in non_basic])
        P = np.transpose(P)
        B_i_inv = np.linalg.inv(B_i)

        z_row = np.dot(np.dot(C_b, B_i_inv), P) - np.array([z[i] for i in non_basic])
        b_i = np.dot(B_i_inv, b)
        x = np.dot(B_i_inv, b)
        z_ = np.dot(C_b, x)

        if all([i >= 0 for i in z_row]):
            res = [0 for _ in range(len(constr[0]))]
            for idx, col in enumerate(basic):
                res[col] = x[idx]
            return res

        entering = np.argmin(z_row)
        B_inv_P = np.dot(B_i_inv, constr[:, non_basic[entering]])
        minimal_arg = 0
        curmin = 999999999999999999999999
        for idx, i in enumerate(B_inv_P):
            if i > 0:
                if curmin > b_i[idx] / i:
                    curmin = b_i[idx] / i
                    minimal_arg = idx

        leaving = minimal_arg
        basic[leaving], non_basic[entering] = non_basic[entering], basic[leaving]


if __name__ == "__main__":
    pass
    # z_f = np.array([9, 10, 16, 0, 0, 0])
    # cond = np.array([
    #     [18, 15, 12, 1, 0, 0],
    #     [6,  4,  8,  0, 1, 0],
    #     [5,  3,  3,  0, 0, 1]
    # ])
    # b_col = np.array([360, 192, 180])
    # z_f = np.array([0, 8, 0, 7, 0, 1])
    # cond = np.array([
    #     [1, -2, 0, -3,  0, -2],
    #     [0,  4, 1, -4,  0, -3],
    #     [0,  5, 0,  5,  1,  1]
    # ])
    # b_col = np.array([12, 12, 25])

    # z_f = np.array([1, 3, 0, -5, 0, 0])
    # cond = np.array([
    #     [2,  4, 1, 2,  0, 0],
    #     [-3,  5, 0, -3,  1, 0],
    #     [4,  -2, 0,  8,  0,  1]
    # ])
    # b_col = np.array([28, 30, 32])

    # z_f = np.array([-2, 1, 0, 1, 0, 0, 0, 0])
    # cond = np.array([
    #     [1, -2,  1,  0, 0,   0, 0, 0],
    #     [-2, -1, 0, -2, -1,  0, 1, 0],
    #     [3,  2,  0,  1, 0,  -1, 0, 1]
    # ])
    # b_col = np.array([10, 18, 36])

    # ans = simplex(z_f, cond, b_col)
    # print(ans)
    # print(np.dot(z_f, ans))
