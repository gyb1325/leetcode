# class Solution:

#     def minSubArrayLen(self, s, nums):
#         """
#         :type s: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         result = len(nums) + 1
#         for idx, n in enumerate(nums[1:], 1):
#             nums[idx] = nums[idx - 1] + n
#         left = 0
#         for right, n in enumerate(nums):
#             if n >= s:
#                 left = self.findleft(left, right, s, nums, n)
#                 result = min(result, right - left + 1)
#         return result if result <= len(nums) else 0

#     def findleft(self, left, right, target, nums, n):
#         while left < right:
#             mid = (left + right) // 2
#             if n - nums[mid] >= target:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left


class Solution:

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        start, end = 0, 0
        total = 0
        min_len = float("inf")
        while end < n:
            total += nums[end]
            end += 1
            while total >= s:
                min_len = min(min_len, end - start)
                total -= nums[start]
                start += 1
        return min_len if min_len != float("inf") else 0
