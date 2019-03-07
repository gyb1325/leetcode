class Solution:

    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ""
        if len(s) < numRows:
            return s
        if numRows <= 1:
            return s
        temp = [""] * numRows
        step = 1
        idx = 0
        for c in s:
            temp[idx] += c
            if idx == 0:
                step = 1
            if idx == numRows - 1:
                step = -1
            idx += step
        return "".join(temp)
