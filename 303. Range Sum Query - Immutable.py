class NumArray:

    def __init__(self, nums: List[int]):
        self.mem = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.mem[i] = self.mem[i - 1] + nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.mem[j + 1] - self.mem[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
