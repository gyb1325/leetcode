class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if matrix[0][0] == "1" else 0
        length = dp[0][0]
        for i in range(m):
            for j in range(n):
                if not i or not j or matrix[i][j] == "0":
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                length = max(length, dp[i][j])
        return length ** 2
