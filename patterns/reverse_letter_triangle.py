#https://www.codingninjas.com/studio/problems/reverse-letter-triangle_6581906?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nLetterTriangle(n: int):
    for i in range(n,-1,-1):
        for j in range(i):
            print(chr(65+j),end=' ')
        print()