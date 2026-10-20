class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        L = 0
        window = set()

        for R in range(len(s)):

            while s[R] in window:
                window.remove(s[L])
                L += 1

            window.add(s[R])

            cur_len = R - L + 1
            max_length = max(max_length, cur_len)

        return max_length