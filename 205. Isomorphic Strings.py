class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m != n:
            return False
        dic1 = {}
        dic2 = {}
        for i in range(m):
            if s[i] in dic1:
                dic1[s[i]].append(i)
            else:
                dic1[s[i]] = [i]
        for i in range(m):
            if t[i] in dic2:
                dic2[t[i]].append(i)
            else:
                dic2[t[i]] = [i]
        for i in range(m):
            if dic1[s[i]] != dic2[t[i]]:
                return False
        return True
