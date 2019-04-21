class Solution:

    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = 0, 0
        n = len(s)
        for i in range(n):
            if s[i] == "(":
                left += 1
            elif s[i] == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1
        res = []
        self.helper(s, left, right, 0, 0, "", res)
        res = list(set(res))
        return res

    def helper(self, s, left, right, local_left, local_right, path, res):
            return
        if not s and left == 0 and right == 0 and local_left == 0 and local_right == 0:
            res.append(path)
            return
        if not s:
            return
        if s[0] == "(":
            if left > 0:
                self.helper(s[1:], left - 1, right, local_left, local_right, path, res)
                self.helper(s[1:], left, right, local_left + 1, local_right, path + s[0], res)
            else:
                self.helper(s[1:], left, right, local_left + 1, local_right, path + s[0], res)
        elif s[0] == ")":
            if right > 0:
                self.helper(s[1:], left, right - 1, local_left, local_right, path, res)
                self.helper(s[1:], left, right, local_left - int(local_left > 0), local_right + 1 - int(local_left > 0), path + s[0], res)
            else:
                self.helper(s[1:], left, right, local_left - int(local_left > 0), local_right + 1 - int(local_left > 0), path + s[0], res)
        else:
            self.helper(s[1:], left, right, local_left, local_right, path + s[0], res)
