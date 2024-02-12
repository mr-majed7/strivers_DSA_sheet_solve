#https://www.codingninjas.com/studio/problems/n-2-forest_6570178?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nForest(n:int) ->None:
    for i in range(n):
        for j in range(i+1):
            print('* ',end='')
        print()