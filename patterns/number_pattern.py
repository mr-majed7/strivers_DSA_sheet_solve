#https://www.codingninjas.com/studio/problems/ninja-and-the-number-pattern-i_6581959?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def getNumberPattern(n: int) -> None:
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            left = j
            right = (2*n-2) - j
            bottom = (2*n-2) - i
            print(n - min(top,left,right,bottom),end='')
        print()