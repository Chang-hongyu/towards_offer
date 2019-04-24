# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 二维数组中的查找
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


def search_2dmatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    j = n - 1
    while i < m and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False


if __name__ == "__main__":
    matrix = [[1, 2, 8, 9],
              [2, 4, 8, 12],
              [4, 7, 10, 13],
              [6, 8, 11, 15],
              [7, 9, 12, 18]]
    target = 12
    ans = search_2dmatrix(matrix, target)
    print(ans)
