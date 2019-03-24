class Solution:

    def convertToTitle(self, n: int) -> str:
        li = []
        while n > 0:
            li.append(chr(ord('A') + (n - 1) % 26))
            n = (n - 1) // 26
        li = li[::-1]
        return "".join(li)
