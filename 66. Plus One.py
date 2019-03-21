class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n - 1, -1, -1):
            temp = digits[i] + carry
            digits[i] = temp % 10
            carry = temp // 10
        return digits if carry == 0 else [1] + digits
