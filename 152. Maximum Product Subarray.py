class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        cur_min = nums[0]
        cur_max = nums[0]
        max_overall = nums[0]
        for num in nums[1:]:
            cur_min, cur_max = min(cur_min * num, cur_max * num, num), max(cur_min * num, cur_max * num, num)
            max_overall = max(cur_max, max_overall)
        return max_overall
