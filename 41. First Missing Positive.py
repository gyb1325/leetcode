class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        # dic = {} # O(n)space
        # n = len(nums)
        # for num in nums:
        #     if num not in dic:
        #         dic[num] = 1
        # for i in range(1, n+2):
        #     if i not in dic:
        #         return i
        nums = list(set(nums)) + [0]  # O(1)space
        n = len(nums)
        for i in range(n):
            if nums[i] >= n or nums[i] < 0:
                nums[i] = 0
        for i in range(n):
            nums[nums[i] % n] += n

        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        return n
