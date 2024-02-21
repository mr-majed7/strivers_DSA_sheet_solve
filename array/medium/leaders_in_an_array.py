#https://www.codingninjas.com/studio/problems/superior-elements_6783446?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse&leftPanelTabValue=PROBLEM

from typing import *


def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    superiors = []
    superiors.append(a[-1])
    max = a[-1]
    for i in range(len(a)-2,-1,-1):
        if a[i] > max:
            superiors.append(a[i])
            max = a[i]
    return superiors