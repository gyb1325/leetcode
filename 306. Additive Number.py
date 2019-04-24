class Solution:

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n // 2 + 1):
            if num[0] = "0" and i > 1:
                break
            for j in range(i + 1, min(j - i, n // 2) + 1)


class Solution:

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        L = len(num)
        for i in range(1, L // 2 + 1):
            if num[0] == '0' and i > 1:
                break
            for j in range(i + 1, min(L - i, (L + i) // 2) + 1):
                if num[i] == '0' and j - i > 1:
                    break
                num1 = num[0:i]
                num2 = num[i:j]
                remain = num[j:]
                if self.isAdditive(num1, num2, remain):
                    return True
        return False

    def isAdditive(self, num1, num2, remain):
        if remain == "":
            return True
        total = str(int(num1) + int(num2))
        if remain.startswith(total):
            return self.isAdditive(num2, total, remain[len(total):])
        else:
            return False
