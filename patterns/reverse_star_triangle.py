#https://www.codingninjas.com/studio/problems/reverse-star-triangle_6573685?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nStarTriangle(n: int) -> None:
    count = 2*n-1
    for i in range(n,0,-1):
        print(' '*(n-i)+'*'*(count)+' '*(n-i))
        count -=2