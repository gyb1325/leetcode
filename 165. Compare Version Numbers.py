class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:

        v1 = version1.split(".")
        v2 = version2.split(".")
        v1 = list(map(int, v1))
        v2 = list(map(int, v2))
        len1 = len(v1)
        len2 = len(v2)
        if len1 > len2:
            for i in range(len1 - len2):
                v2 = v2 + [0]
        else:
            for i in range(len2 - len1):
                v1 = v1 + [0]
        a1 = 0
        a2 = 0
        for i in range(len(v1)):
            a1 = a1 * 10 + v1[i]
            a2 = a2 * 10 + v2[i]
        if a1 > a2:
            return 1
        elif a1 < a2:
            return -1
        else:
            return 0
