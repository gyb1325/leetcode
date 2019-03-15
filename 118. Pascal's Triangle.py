class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        row = 2
        while row < numRows:
            temp = [1]
            for i in range(len(res[row - 1]) - 1):
                temp.append(res[row - 1][i] + res[row - 1][i + 1])

            temp.append(1)
            res.append(temp)
            row += 1
        return res
