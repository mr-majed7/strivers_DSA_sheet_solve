#https://www.codingninjas.com/studio/problems/seeding_6581892?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def seeding(n: int) -> None:
    for i in range(n,0,-1):
        for j in range(i):
            print('* ',end='')
        print()