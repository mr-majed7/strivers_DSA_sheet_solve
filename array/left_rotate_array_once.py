#https://www.codingninjas.com/studio/problems/left-rotate-an-array-by-one_5026278?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

from collections import *
from math import *
from sys import *


def rotateArray(arr: [], n: int) -> []:
    for i in range(1):
        for j in range(n-1):
            arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr
