#https://www.codingninjas.com/studio/problems/alpha-hill_6581921?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def alphaHill(n: int):
    char = 65
    for i in range(n):
        print(' '*(n-i-1),end='')
        for j in range(i+1):
            print(chr(char),end=' ')
            char +=1
        char -=1
        for k in range(i):
            char -=1
            print(chr(char),end=' ')
        print((' '*(n-i-1)))
        char = 65
        print()