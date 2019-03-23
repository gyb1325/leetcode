class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            reutrn
        n = len(matrix[0])

        setr = set()
        setc = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    setr.add(i)
                    setc.add(j)
        for item in setr:
            for c in range(n):
                matrix[item][c] = 0

        for item in setc:
            for r in range(m):
                matrix[r][item] = 0
