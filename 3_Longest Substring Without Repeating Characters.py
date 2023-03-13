class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_idx = {}
        max_len = 0
        start = end = 0
        while end < len(s):
            if s[end] in s_idx.keys() and s_idx[s[end]] >= start:
                start = s_idx[s[end]] + 1
            s_idx[s[end]] = end
            max_len = max(max_len, end-start+1)
            end += 1

        return max_len
