# https://www.interviewbit.com/problems/nearest-smaller-element/

class Solution:
	# @param A : list of integers
	# @return a list of integers
    def prevSmaller(self, A):
        nse = []
        st = []
        for i in A:
            while st:
                if st[-1] < i:
                    nse.append(st[-1])
                    st.append(i)
                    break
                else:
                    st.pop()
            if not st:
                nse.append(-1)
                st.append(i)
        return nse
