# https://www.codingninjas.com/studio/problems/longest-successive-elements_6811740?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from typing import *


def longestSuccessiveElements(a: List[int]) -> int:
    """
    First we take the unique elements from the list and store them in a set.
    Then we iterate over the set and check if the element-1 is not present in the set.
    If a element - 1 is not in the array that means it is the first element of a sequence.
    If it is not present then we start counting the number of elements that are present in the set starting from the current element.
    We keep track of the longest count and return it.
    """
    n = len(a)
    if n == 0:
        return 0

    st = set()
    longest = 1

    for n in a:
        st.add(n)

    for n in st:
        if n - 1 not in st:
            count = 1
            x = n

            while x + 1 in st:
                x += 1
                count += 1
            longest = max(count, longest)
    return longest
