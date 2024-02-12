#https://www.codingninjas.com/studio/problems/triangle_6573690?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def triangle( n:int) ->None:
    for i in range(1,n+1):
        for j in range(i):
            print(i,' ',end='')
        print()