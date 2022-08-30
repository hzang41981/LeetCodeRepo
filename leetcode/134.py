class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # -2, -2, -2, 3, 3, -7, 8

        for i in range(len(gas)):
            gas[i] -= cost[i]
        curr = 0
        curr_start_idx = 0
        for pter in range(len(gas)):
            curr += gas[pter]
            if curr >= 0 and pter - curr_start_idx == len(gas):
                return curr_start_idx
            if curr < 0:
                curr_start_idx = pter + 1
                curr = 0
        print(gas, curr, curr_start_idx)
        if curr == 0 and curr_start_idx == 0:
            return 0
        if curr > 0:
            for i in range(0, curr_start_idx):
                curr += gas[i]
                if curr < 0:
                    return -1
            if curr >= 0:
                return curr_start_idx
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.canCompleteCircuit([3,1,1], [1,2,2]))


