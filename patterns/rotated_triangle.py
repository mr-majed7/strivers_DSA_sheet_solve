#https://www.codingninjas.com/studio/problems/rotated-triangle_6573688?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION

def nStarTriangle(n: int) -> None:
    count = 0
    for i in range(n):
        count +=1
        print('*'*count)
    for j in range(n-1):
        count -=1
        print('*'*count)