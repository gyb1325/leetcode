class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_val = float("inf")
        self.stack = []

    def push(self, x: int) -> None:
        if x <= self.min_val:
            self.stack.append(self.min_val)
            self.min_val = x
        self.stack.append(x)

    def pop(self) -> None:
        if (self.stack.pop() == self.min_val):
            self.min_val = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
