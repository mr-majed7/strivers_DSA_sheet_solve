#https://www.codingninjas.com/studio/problems/n-forest_6570177?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nForest(n:int) ->None:
    for i in range(n):
        for j in range(n):
            print('* ',end='')
        print()