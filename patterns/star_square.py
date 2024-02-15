#https://www.codingninjas.com/studio/problems/ninja-and-the-star-pattern-i_6581920?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def getStarPattern(n: int) -> None:
    for i in range(n):
        if i==0 or i==n-1:
            print('*'*n)
        else:
            print(('*')+' '*(n-2)+'*')