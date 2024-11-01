# https://leetcode.com/problems/remove-k-digits/
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) ==k:
            return "0"
        
        st = []

        for n in num:
            while st and k >0 and int(st[-1])>int(n):
                st.pop()
                k -=1
            
            st.append(n)
  
        while k>0:
            st.pop()
            k -=1
        
        if len(st)==0:
            return "0"  
        
        string = ""

        for n in st:
            if len(string) == 0 and n == "0":
                continue
            string +=n
        
        return "0" if len(string) == 0 else string
