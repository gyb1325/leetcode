class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in dict:
                return [dict[target - num], i]
            else:
                dict[num] = i
        return []
