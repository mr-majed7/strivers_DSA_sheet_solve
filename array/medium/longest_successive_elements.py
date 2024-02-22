#https://www.codingninjas.com/studio/problems/longest-successive-elements_6811740?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from typing import *


def longestSuccessiveElements(a : List[int]) -> int:
    n = len(a)
    if n == 0:
        return 0

    st = set()
    longest = 1

    for n in a:
        st.add(n)

    for n in st:
        if n-1 not in st:
            count = 1
            x = n

            while x+1 in st:
                x +=1
                count +=1
            longest = max(count,longest)
    return longest
    
