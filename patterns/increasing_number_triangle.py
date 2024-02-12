#https://www.codingninjas.com/studio/problems/increasing-number-triangle_6581893?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nNumberTriangle(n: int) -> None:
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num,end=' ')
            num +=1
        print()