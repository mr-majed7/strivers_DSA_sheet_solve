#https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from collections import *
from math import *
from sys import *


def largestElement(arr: [], n: int) -> int:

    max = 0
    for i in arr:
        if i > max:
            max = i
    return max
