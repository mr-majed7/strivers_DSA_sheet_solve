# https://www.codingninjas.com/studio/problems/superior-elements_6783446?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse&leftPanelTabValue=PROBLEM

from typing import *


def superiorElements(a: List[int]) -> List[int]:
    """
    The last element of the array is always a superior element.
    We start from the second last element and compare it with the last superior element.
    If the current element is greater than the last superior element, then it is also a superior element.
    We keep track of the maximum element found so far and compare it with the current element.
    If the current element is greater than the maximum element found so far, then it is also a superior element.
    """
    # Write your code here.
    superiors = []  # list to store the superior elements
    superiors.append(a[-1])  # last element is always a superior element
    max = a[-1]  # maximum element found so far
    for i in range(len(a) - 2, -1, -1):
        if (
            a[i] > max
        ):  # if the current element is greater than the maximum element found so far
            superiors.append(a[i])  # then it is also a superior element
            max = a[i]  # update the maximum element found so far
    return superiors
