#https://www.codingninjas.com/studio/problems/increasing-letter-triangle_6581897?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nLetterTriangle(n: int) -> None:
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j),end=' ')
        print()