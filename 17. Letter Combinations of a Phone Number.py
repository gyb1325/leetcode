class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        self.table = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        self.backtracking(digits, "", res)
        return res

    def backtracking(self, digits, path, res):
        if digits == "":
            res.append(path)
            return
        for c in self.table[int(digits[0])]:
            self.backtracking(digits[1:], path + c, res)
