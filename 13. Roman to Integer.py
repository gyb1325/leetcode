class Solution:

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = str(s)
        lst1 = {'CM': 900, 'CD': 400, 'XL': 40, 'XC': 90, 'IV': 4, 'IX': 9}
        lst2 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        if not s:
            return 0
        if len(s) == 1:
            return lst2[s]
        i = 0
        sum = 0
        while i <= len(s) - 1:
            if len(s[i:]) >= 2 and s[i:i + 2] in lst1:
                sum += lst1[s[i:i + 2]]
                i += 2
            else:
                sum += lst2[s[i]]
                i += 1
        return sum
