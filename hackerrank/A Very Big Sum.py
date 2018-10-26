#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
res = sum(arr)
print(res)
