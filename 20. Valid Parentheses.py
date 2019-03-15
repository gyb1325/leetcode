class Solution:

    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        stack = []
        for c in s:
            if c in "[({":
                stack.append(c)
            else:
                if stack:
                    temp = stack.pop()
                    if ord(c) - ord(temp) == 2 or ord(c) - ord(temp) == 1:
                        continue
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
