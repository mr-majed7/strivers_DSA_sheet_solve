#https://www.codingninjas.com/studio/problems/star-diamond_6573686?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nStarDiamond(n: int) -> None:
    count = 1
    for i in range(n):
        print(' '*(n-i-1)+'*'*count+' '*(n-i-1))
        count +=2
    for j in range(n,0,-1):
        count -=2
        print(' '*(n-j)+'*'*(count)+' '*(n-j))