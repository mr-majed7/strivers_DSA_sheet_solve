#https://www.codingninjas.com/studio/problems/reverse-number-triangle_6581889?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nNumberTriangle(n: int) -> None:
    for i in range(n,0,-1):
        for j in range(i):
            print(j+1,' ',end='')
        print()