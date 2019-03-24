class Solution:

    def titleToNumber(self, s: str) -> int:
        cnt = 0
        res = 0
        for c in s[::-1]:
            res += (ord(c) - ord("A") + 1) * 26**cnt
            cnt += 1
        return res
