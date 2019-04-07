class Solution:

    def calculate(self, s: str) -> int:
        stack = []
        num = "1234567890"
        number = 0
        sign = 1
        result = 0
        for c in s:
            if c in num:
                number = 10 * number + int(c)
            elif c == "+":
                result += sign * number
                number = 0
                sign = 1
            elif c == "-":
                result += sign * number
                number = 0
                sign = -1
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ")":
                result += sign * number
                number = 0
                sign = stack.pop()
                prev = stack.pop()
                result = sign * result + prev
        if number:
            return result + number * sign
        else:
            return result
