class Solution:

    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "+-*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i + 1:])
                for k in res1:
                    for j in res2:
                        res.append(self.helper(k, j, input[i]))
        return res

    def helper(self, i, j, op):
        if op == "+":
            return i + j
        elif op == "-":
            return i - j
        else:
            return i * j
