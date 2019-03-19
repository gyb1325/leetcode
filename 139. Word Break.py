class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if s[i - len(w) + 1:i + 1] == w and (d[i - len(w)] or i - len(w) == -1):
                    d[i] = True
        return d[-1]
