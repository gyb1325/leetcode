class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        l, r = 0, len(matrix[0]) - 1
        u, d = 0, len(matrix) - 1
        res = []
        while l <= r and u <= d:
            for i in range(l, r + 1):
                res.append(matrix[u][i])
            u += 1

            for i in range(u, d + 1):
                res.append(matrix[i][r])

            r -= 1

            if u <= d:
                for i in range(r, l - 1, -1):
                    res.append(matrix[d][i])

            d -= 1

            if l <= r:
                for i in range(d, u - 1, -1):
                    res.append(matrix[i][l])
            l += 1
        return res
