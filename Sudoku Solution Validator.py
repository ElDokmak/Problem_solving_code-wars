import numpy as np


def valid_square(array):
    sum = 0
    x = 0
    res = np.zeros(9)
    for i_o in range(0, 9, 3):
        for j_o in range(0, 9, 3):
            for i in range(3):
                for j in range(3):
                    sum = sum + array[i_o + i][j_o + j]
            res[x] = sum
            if res[x] != 45:
                return False
            sum = 0
            x = x + 1
    if res.sum() == 405:
        return True


def valid_solution(validSolution):
    array = valid_solution
    check_1 = np.zeros(9)
    check_2 = np.zeros(9)
    for i in range(9):
        row = 0
        col = 0
        for j in range(9):
            row = row + validSolution[i][j]
            col = col + validSolution[j][i]
        check_1[i] = row
        check_2[i] = col
    for x in range(9):
        if check_1[x] != 45:
            return False
        if check_2[x] != 45:
            return False
    if check_1.sum() == 405:
        ans = valid_square(validSolution)
        return ans
    else:
        return False


print(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8], [4, 9, 8, 2, 6, 1, 3, 7, 5], [7, 5, 6, 3, 8, 4, 2, 1, 9], [6, 4, 3, 1, 5, 8, 7, 9, 2], [
      5, 2, 1, 7, 9, 3, 8, 4, 6], [9, 8, 7, 4, 2, 6, 5, 3, 1], [2, 1, 4, 9, 3, 5, 6, 8, 7], [3, 6, 5, 8, 1, 7, 9, 2, 4], [8, 7, 9, 6, 4, 2, 1, 3, 5]]))
