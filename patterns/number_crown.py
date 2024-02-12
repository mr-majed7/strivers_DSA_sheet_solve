#https://www.codingninjas.com/studio/problems/number-crown_6581894?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def numberCrown(n: int) -> None:
    space = 2*n
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=' ')
        
        print(' '*space,end='')

        for k in range(i+1,0,-1):
            print(k,end=' ')
        space -=2
        print()
