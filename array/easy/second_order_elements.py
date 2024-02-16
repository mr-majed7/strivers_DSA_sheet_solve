#https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    largest = float('-inf')
    secondLargest = float('-inf')
    smallest = float('inf')
    secondSmallest = float('inf')
    
    for i in a:
        if i >= largest:
            secondLargest = largest
            largest = i
        elif i >= secondLargest:
            secondLargest = i
        
        if i <= smallest:
            secondSmallest = smallest
            smallest = i
        elif i <= secondSmallest:
            secondSmallest = i
    
    return [secondLargest, secondSmallest]