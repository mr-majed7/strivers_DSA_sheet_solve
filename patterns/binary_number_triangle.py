#https://www.codingninjas.com/studio/problems/binary-number-triangle_6581890?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nBinaryTriangle(n: int) -> None:
    num1 = 1
    for i in range(n):
        num = num1
        for j in range(i+1):
            print(num,end=' ')
            num = 0 if num == 1 else 1
        num1 = 0 if num1 == 1 else 1
        print()