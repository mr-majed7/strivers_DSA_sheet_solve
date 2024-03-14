# https://www.codingninjas.com/studio/problems/ceiling-in-a-sorted-array_1825401?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


def getFloorAndCeil(a, n, x):
    # Write your code here.
    low = 0
    high = n - 1
    floor = -1
    celi = -1

    while low <= high:
        mid = (low + high) // 2
        if a[mid] <= x:
            floor = a[mid]
            low = mid + 1
        else:
            high = mid - 1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] >= x:
            celi = a[mid]
            high = mid - 1
        else:
            low = mid + 1
    return [floor, celi]
