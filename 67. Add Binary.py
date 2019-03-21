class Solution:

    def addBinary(self, a: str, b: str) -> str:
        new = ""
        m = len(a) - 1
        n = len(b) - 1
        carry = 0
        while m >= 0 and n >= 0:
            temp = int(a[m]) + int(b[n]) + carry
            new = str(temp % 2) + new
            carry = temp // 2
            m -= 1
            n -= 1
        while m >= 0:
            temp = int(a[m]) + carry
            new = str(temp % 2) + new
            carry = temp // 2
            m -= 1
        while n >= 0:
            temp = int(b[n]) + carry
            new = str(temp % 2) + new
            carry = temp // 2
            n -= 1
        return new if not carry else "1" + new
