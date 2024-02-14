#https://www.codingninjas.com/studio/problems/rotate-array_1230543?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

def rotateArray(arr: list, k: int) -> list:
    k = k%len(arr)

    arr = arr[k:] + arr[:k]

    return arr 