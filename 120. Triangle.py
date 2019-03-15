class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Naive Method
        # n = len(triangle)
        # a = [[float("inf")] * n for _ in range(n)]
        # a[0][0] = triangle[0][0]
        # for row in range(1, n):
        #     m = len(triangle[row])
        #     for i in range(m):
        #         if i > 0 and i < m - 1:
        #             a[row][i] = triangle[row][i] + min(a[row - 1][i], a[row - 1][i - 1])
        #         elif i == 0:
        #             a[row][i] = triangle[row][i] + a[row - 1][i]
        #         else:
        #             a[row][i] = triangle[row][i] + a[row - 1][i - 1]
        # return min(a[n - 1])
        # O(n) space
        n = len(triangle)
        a = [float("inf")] * n
        a[0] = triangle[0][0]
        for row in range(1, n):
            m = len(triangle[row])
            for i in range(m - 1, -1, -1):
                if i > 0 and i < m - 1:
                    a[i] = triangle[row][i] + min(a[i], a[i - 1])
                elif i == m - 1:
                    a[i] = triangle[row][i] + a[i - 1]
                else:
                    a[i] = triangle[row][i] + a[i]
        return min(a)
