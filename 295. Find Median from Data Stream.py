from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        heappush(self.large, num)
        heappush(self.small, -heappop(self.large))
        if len(self.large) < len(self.small):
            heappush(self.large, -heappop(self.small))

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return float(self.large[0])
        else:
            return (self.large[0] - self.small[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
