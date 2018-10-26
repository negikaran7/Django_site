#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zero_count=0
    pos_count=0
    neg_count=0
    for i in range(len(arr)):
        if arr[i]>0:
            pos_count+=1
        elif arr[i]<0:
            neg_count+=1
        elif arr[i]==0:
            zero_count+=1
    
    print(pos_count/n)
    print(neg_count/n)
    print(zero_count/n)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
