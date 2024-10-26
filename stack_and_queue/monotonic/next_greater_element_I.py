# https://leetcode.com/problems/next-greater-element-i/description/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nge = {}
        st = []

        for i in range(len(nums2) - 1, -1, -1):
            while st:
                if st[-1] > nums2[i]:
                    nge[nums2[i]] = st[-1]
                    st.append(nums2[i])
                    break
                else:
                    st.pop()
            if not st:
                nge[nums2[i]] = -1
                st.append(nums2[i])

        for j in nums1:
            ans.append(nge[j])
        return ans
