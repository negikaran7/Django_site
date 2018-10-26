#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
# def diagonalDifference(arr):
sum_diag1 = 0
sum_diag2 = 0
n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    sum_diag1 += a_t[a_i]
    sum_diag2 += a_t[(n - 1) - a_i]
    res = abs(sum_diag1 - sum_diag2)
print(res)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(input())
#     arr = []
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#     result = diagonalDifference(arr)
#     fptr.write(str(result) + '\n')
#     fptr.close()
