from random import randint


class Solution:

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        target = len(nums) - k
        return self.helper(nums, target)

    def helper(self, nums, target):
        i = randint(0, len(nums) - 1)
        pivot = nums[i]
        nums[i], nums[0] = nums[0], nums[i]
        a = [x for x in nums if x < pivot]
        b = [x for x in nums[1:] if x >= pivot]
        if len(a) == target:
            return pivot
        elif len(a) < target:
            return self.helper(b, target - len(a) - 1)
        elif len(a) > target:
            return self.helper(a, target)


# use Heap to implement
import heapq


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            if len(q) < k:
                heapq.heappush(q, num)
            else:
                if num > q[0]:
                    heapq.heappop(q)
                    heapq.heappush(q, num)
        return q[0]
