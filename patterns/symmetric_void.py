#https://www.codingninjas.com/studio/problems/symmetric-void_6581919?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def symmetry(n: int):  
    space = 0
    for i in range(n,0,-1):
        print(('* ')*i+' '*space+('* ')*i)
        space +=2
    space -=2
    for k in range(1,n+1):
        print(('* ')*k+' '*space+('* ')*k)
        space -=2
