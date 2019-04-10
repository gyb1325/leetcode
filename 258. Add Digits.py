class Solution:

    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        temp = 0
        while num > 0:
            temp += num % 10
            num = num // 10
        return self.addDigits(temp)
