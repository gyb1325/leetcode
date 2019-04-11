class Solution:

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        v_array = primes.copy()
        ptr = [0] * len(primes)
        while n > 1:
            umin = min(v_array)
            ugly.append(umin)
            for i in range(len(primes)):
                if umin == v_array[i]:
                    ptr[i] += 1
                    v_array[i] = ugly[ptr[i]] * primes[i]
            n -= 1
        return ugly[-1]
