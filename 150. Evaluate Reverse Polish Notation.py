class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = ["+", "-", "*", "/"]
        s = set(s)
        for item in tokens:
            if item not in s:
                stack.append(int(item))
            else:
                if item == "+":
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    stack.append(temp1 + temp2)
                elif item == "-":
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    stack.append(temp2 - temp1)
                elif item == "*":
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    stack.append(temp2 * temp1)
                else:
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    if temp1 * temp2 >= 0:
                        stack.append(temp2 // temp1)
                    else:
                        temp_result = abs(temp2) // abs(temp1)
                        stack.append(-1 * temp_result)
        return stack[-1]
