class Solution:

    def minCut(self, s: str) -> int:
        #             res = [float("inf")]
        #             self.dfs(s, [], res)
        #             return res[0]

        #     def dfs(self, temp_str, path, res):
        #         if len(path) - 1 >=res[0]:
        #             return
        #         if temp_str == "":
        #             if len(path) - 1 < res[0]:
        #                 res[0] = len(path) - 1
        #             return
        #         for i in range(1, len(temp_str)+1):
        #             if self.isP(temp_str[:i]):
        #                 self.dfs(temp_str[i:], path + [temp_str[:i]], res)

        #     def isP(self, s):
        #         return s == s[::-1]

        m = len(s)
        d = [0] * m
        pal = [[False] * m for _ in range(m)]
        for i in range(m - 1, -1, -1):
            d[i] = m - 1 - i
            for j in range(i, m):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True
                    if j == m - 1:
                        d[i] = 0
                    elif(d[i] > d[j + 1] + 1):
                        d[i] = d[j + 1] + 1
        return d[0]
