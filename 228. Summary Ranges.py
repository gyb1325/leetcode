class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        temp_store = []
        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                end = nums[i]
            else:
                if start == end:
                    temp_store.append([str(start)])
                else:
                    temp_store.append([str(start), str(end)])
                start = end = nums[i]
        if start == end:
            temp_store.append([str(start)])
        else:
            temp_store.append([str(start), str(end)])
        res = []
        for lst in temp_store:
            if len(lst) == 1:
                res.append(lst[0])
            else:
                res.append("->".join(lst))
        return res


class Solution:

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        range = []
        for n in nums:
            if (not range) or range[-1][-1] + 1 < n:
                range.append([])
            range[-1][1:] = [n]
        return [("->").join(map(str, r)) for r in range]
