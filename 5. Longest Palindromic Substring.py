class Solution:

    def longestPalindrome(self, s: str) -> str:

        max_len = 0
        max_str = ""
        for i in range(len(s)):
            temp = self.helper(i, i, s)
            if len(temp) > max_len:
                max_str = temp
                max_len = len(temp)
        for i in range(len(s)):
            temp = self.helper(i, i + 1, s)
            if len(temp) > max_len:
                max_str = temp
                max_len = len(temp)
        return max_str

    def helper(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
