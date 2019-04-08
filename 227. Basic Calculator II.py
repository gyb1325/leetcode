class Solution:

    def calculate(self, s: str) -> int:
        if not s:
            return 0
        sign = "+"
        stack = []
        num = 0
        numbers = "0123456789"
        for i, c in enumerate(s):
            if c in numbers:
                num = num * 10 + int(c)
            if c in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    temp = stack.pop()
                    if temp // num < 0 and temp % num != 0:
                        stack.append(temp // num + 1)
                    else:
                        stack.append(temp // num)
                sign = c
                num = 0
        # if num != 0:
        #     stack.append(num)
        return sum(stack)
