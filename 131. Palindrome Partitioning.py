class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, temp_str, path, res):
        if temp_str == "":
            res.append(path)
            return
        for i in range(1, len(temp_str) + 1):
            if self.isP(temp_str[:i]):
                self.dfs(temp_str[i:], path + [temp_str[:i]], res)

    def isP(self, s):
        return s == s[::-1]
