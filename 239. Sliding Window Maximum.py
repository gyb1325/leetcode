class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Naive Method
        if not nums:
            return []
        cur_largest = max(nums[0:k])
        res = [cur_largest]
        for i in range(k, len(nums)):
            if nums[i] >= cur_largest:
                res.append(nums[i])
                cur_largest = nums[i]
            else:
                cur_largest = max(nums[i+1-k:i+1])
                res.append(cur_largest)
        return res
        '''
        q = collections.deque()
        res = []
        for i in range(len(nums)):
            if q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
