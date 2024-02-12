#https://www.codingninjas.com/studio/problems/alpha-ramp_6581888?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def alphaRamp(n: int) -> None:
    char = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(char),end=' ')
        print()
        char +=1