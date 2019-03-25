class Solution:

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = {}
        res = set()
        length = len(s) - 10 + 1
        for i in range(length):
            if s[i:i + 10] in dic:
                res.add(s[i:i + 10])
            else:
                dic[s[i:i + 10]] = 0
        return list(res)
