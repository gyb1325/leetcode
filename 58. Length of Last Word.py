class Solution:

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = (s.strip()).split(" ")
        if a != []:
            return len(a[-1])
        else:
            return 0
