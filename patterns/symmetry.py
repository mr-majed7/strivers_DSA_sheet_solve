#https://www.codingninjas.com/studio/problems/symmetry_6581914?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def symmetry(n: int):
    space = 2*n
    for i in range(1,n+1):
        space -=2
        print('* '*i+' '*space+'* '*i)
        space -=2
    for j in range(n-1,0,-1):
        space +=2
        print('* '*j+' '*space+'* '*j)