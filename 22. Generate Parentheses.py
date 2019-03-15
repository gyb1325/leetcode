class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = n
        right = n
        ans = []
        self.dfs(n, n, ans, "")
        return ans

    def dfs(self, left, right, ans, s):
        if right < left:
            return
        if left == 0 and right == 0:
            ans.append(s)
        if left:
            self.dfs(left - 1, right, ans, s + "(")
        if right:
            self.dfs(left, right - 1, ans, s + ")")
