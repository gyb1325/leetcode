class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        row = 2
        prev = [1, 1]
        while row <= rowIndex:
            temp = [1]
            for i in range(len(prev) - 1):
                temp.append(prev[i] + prev[i + 1])
            temp.append(1)
            prev = temp
            row += 1
        return prev
