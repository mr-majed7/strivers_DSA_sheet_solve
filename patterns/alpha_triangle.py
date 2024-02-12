#https://www.codingninjas.com/studio/problems/alpha-triangle_6581429?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def alphaTriangle(n: int):
    char = 64+n
    for i in range(n):
        for j in range(i+1):
            print(chr(char-j),end=' ')
        print()