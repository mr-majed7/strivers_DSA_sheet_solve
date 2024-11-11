# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = [-1, -1, -1]
        count = 0

        for i in range(len(s)):
            last_seen[ord(s[i]) - ord("a")] = i

            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
                count += 1 + min(last_seen[0], last_seen[1], last_seen[2])
        return count
