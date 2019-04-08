class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        self.stack2 = []
        for item in self.stack1[::-1]:
            self.stack2.append(item)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        temp = self.stack2.pop()
        self.stack1 = []
        for item in self.stack2[::-1]:
            self.stack1.append(item)
        return temp

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
