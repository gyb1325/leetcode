class Solution:

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lst = str.split(" ")
        dic1 = {}
        dic2 = {}
        m = len(pattern)
        n = len(lst)
        if m != n:
            return False

        for i in range(m):
            if pattern[i] not in dic1:
                if lst[i] not in dic2:
                    dic1[pattern[i]] = lst[i]
                    dic2[lst[i]] = pattern[i]
                else:
                    return False
            else:
                if dic1[pattern[i]] == lst[i] and dic2[lst[i]] == pattern[i]:
                    continue
                else:
                    return False

        return True
