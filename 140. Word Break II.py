class Solution:
    # Time Exceeded result, 'cause I do not remember the thing I searched before'
    #     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    #         res = []
    #         wordDict = set(wordDict)
    #         self.helper(s, wordDict, "", res)
    #         return res

    #     def helper(self, s, wordDict, path, res ):
    #         if not s:
    #             res.append(path)
    #         for i in range(len(s)):
    #             if s[:i+1] in wordDict:
    #                 if not path:
    #                     self.helper(s[i+1:], wordDict, path+s[:i+1], res)
    #                 else:
    #                     self.helper(s[i+1:], wordDict, path+" "+s[:i+1], res)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, dic):
        if s in dic:
            return dic[s]
        if not s:
            return []
        res = []
        for w in wordDict:
            if not s.startswith(w):
                continue
            elif len(s) == len(w):
                res.append(w)
            else:
                temp = self.helper(s[len(w):], wordDict, dic)
                for item in temp:
                    item = w + " " + item
                    res.append(item)
        dic[s] = res
        return res
