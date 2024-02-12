#https://www.codingninjas.com/studio/problems/star-triangle_6573671?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nStarTriangle(n: int) -> None:
    count = 1
    for i in range(n):
        print(' '*(n-i-1)+'*'*count+' '*(n-i-1))
        count +=2