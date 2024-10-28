# https://leetcode.com/problems/next-greater-element-ii/submissions/1436352031/
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nge = []
        st = []
        N = len(nums)

        for i in range(2 * N, -1, -1):
            while st and st[-1] <= nums[i % N]:
                st.pop()
            if i < N:
                nge.append(-1 if len(st) == 0 else st[-1])
            st.append(nums[i % N])
        return nge[::-1]
