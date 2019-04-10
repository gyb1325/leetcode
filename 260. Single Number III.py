# Naive Solution


class Solution:

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            if i in dic:
                del dic[i]
            else:
                dic[i] = 0
        return list(dic.keys())

# O(1) Space


class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = nums[0]
        for num in nums[1:]:
            temp ^= num
        new_temp = 1
        while True:
            if new_temp & temp:
                break
            new_temp = new_temp << 1
        temp1 = 0
        temp2 = 0
        for num in nums:
            if num & new_temp == 0:
                temp1 ^= num
            else:
                temp2 ^= num
        return [temp1, temp2]
