class Solution:

    def shortestPalindrome(self, s: str) -> str:
        pattern = s + "#" + s[::-1]
        n = len(pattern)
        aux_array = [0] * n
        self.compute_array(pattern, aux_array)
        pali = aux_array[-1]
        non_pali = s[pali:]
        return non_pali[::-1] + s

    def compute_array(self, pattern, aux_array):
        n = len(pattern)
        i, j = 1, 0
        while i < n:
            if pattern[i] == pattern[j]:
                aux_array[i] = j + 1
                i += 1
                j += 1
            else:
                if j != 0:
                    j = aux_array[j - 1]
                else:
                    aux_array[i] = 0
                    i += 1
