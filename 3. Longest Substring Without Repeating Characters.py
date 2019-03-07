class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l = 0
        r = 1
        max_len = 0
        dic = {s[0]: 0}
        while r < len(s):
            if s[r] in dic:
                max_len = max(max_len, r - l)
                if l <= dic[s[r]] + 1:
                    l = dic[s[r]] + 1
                dic[s[r]] = r
                r += 1
            else:
                dic[s[r]] = r
                r += 1
                max_len = max(max_len, r - l)
        max_len = max(max_len, r - l)

        return max_len
