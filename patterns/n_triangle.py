#https://www.codingninjas.com/studio/problems/n-triangles_6573689?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nTriangle(n:int) ->None:
    for i in range(n):
        for j in range(i+1):
            print(j+1,' ',end='')
        print()