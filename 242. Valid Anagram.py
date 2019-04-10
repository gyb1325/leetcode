class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for c in t:
            if c not in dic:
                return False
            if dic[c] < 1:
                return False
            dic[c] -= 1
        return True
