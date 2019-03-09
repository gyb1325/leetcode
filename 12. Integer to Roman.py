class Solution:

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        lst = []
        while num > 0:
            if num - 1000 >= 0:
                lst.append("M")
                num -= 1000
                continue
            if num - 900 >= 0:
                lst.append("CM")
                num -= 900
                continue
            if num - 500 >= 0:
                lst.append("D")
                num -= 500
                continue
            if num - 400 >= 0:
                lst.append("CD")
                num -= 400
                continue
            if num - 100 >= 0:
                lst.append("C")
                num -= 100
                continue
            if num - 90 >= 0:
                lst.append("XC")
                num -= 90
                continue
            if num - 50 >= 0:
                lst.append("L")
                num -= 50
                continue
            if num - 40 >= 0:
                lst.append("XL")
                num -= 40
                continue
            if num - 10 >= 0:
                lst.append("X")
                num -= 10
                continue
            if num - 9 >= 0:
                lst.append("IX")
                num -= 9
                continue
            if num - 5 >= 0:
                lst.append("V")
                num -= 5
                continue
            if num - 4 >= 0:
                lst.append("IV")
                num -= 4
                continue
            if num - 3 >= 0:
                lst.append("III")
                num -= 3
                continue
            if num - 2 >= 0:
                lst.append("II")
                num -= 2
                continue
            if num - 1 >= 0:
                lst.append("I")
                num -= 1
                continue
        return "".join(lst)
