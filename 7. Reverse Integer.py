class Solution:

    def reverse(self, x: int) -> int:

        s = str(x)
        temp = ""
        if s[0] == "-":
            s = s[1:]
            temp = s[::-1]
        else:
            temp = s[::-1]
        for i in range(len(temp)):
            if temp[i] != "0":
                break
        temp = temp[i:]
        if x <= 0:
            temp = "-" + temp
        if int(temp) > 2**31 - 1 or int(temp) < -2**31:
            return 0
        else:
            return int(temp)
