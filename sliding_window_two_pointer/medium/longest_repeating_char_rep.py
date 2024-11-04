# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = [0] * 26
        max_length = 0
        max_freq = 0
        left = 0

        for right in range(len(s)):
            char_map[ord(s[right]) - ord("A")] += 1
            max_freq = max(max_freq, char_map[ord(s[right]) - ord("A")])

            if (right - left + 1) - max_freq > k:
                char_map[ord(s[left]) - ord("A")] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
