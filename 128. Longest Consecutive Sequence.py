class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        dic = {}
        for num in nums:
            if num not in dic:
                left = dic.get(num - 1, 0)
                right = dic.get(num + 1, 0)
                sum = left + right + 1
                dic[num] = sum
                res = max(res, sum)
                dic[num - left] = sum
                dic[num + right] = sum
            else:
                continue
        return res
