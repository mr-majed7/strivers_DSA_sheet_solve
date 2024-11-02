# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = [-1] * 256
        max_length = 0

        left = 0
        right = 0

        while right < len(s):
            if char_map[ord(s[right])] != -1:
                left = max(char_map[ord(s[right])] + 1, left)


            char_map[ord(s[right])] = right


            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
