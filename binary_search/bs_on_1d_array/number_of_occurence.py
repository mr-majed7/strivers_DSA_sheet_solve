# https://www.codingninjas.com/studio/problems/occurrence-of-x-in-a-sorted-array_630456?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


def count(arr: [int], n: int, x: int) -> int:
    # Your code goes here
    low = 0
    high = n - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            first = mid
            high = mid - 1
        else:
            low = mid + 1
    low = 0
    high = n - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    if first == -1 or last == -1:
        return 0
    return last - first + 1
