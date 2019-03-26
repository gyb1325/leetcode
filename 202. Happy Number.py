class Solution:

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        mem = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in mem:
                return False
            mem.add(n)
        return True
