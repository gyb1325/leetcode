class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:
        new = [[0] * n for i in range(n)]

        l, r = 0, n - 1
        u, d = 0, n - 1
        cnt = 1
        while l <= r and u <= d:
            for i in range(l, r + 1):
                new[u][i] = cnt
                cnt += 1
            u += 1

            for i in range(u, d + 1):
                new[i][r] = cnt
                cnt += 1

            r -= 1

            if u <= d:
                for i in range(r, l - 1, -1):
                    new[d][i] = cnt
                    cnt += 1

            d -= 1

            if l <= r:
                for i in range(d, u - 1, -1):
                    new[i][l] = cnt
                    cnt += 1
            l += 1
        return new
