class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        balance = 0
        position = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                balance = 0
                position = i + 1
        return position
