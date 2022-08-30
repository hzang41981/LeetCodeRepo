import random
from collections import Counter
import heapq
class Solution:
    def topKFrequent2(self, nums, k):
        if k == len(nums):
            return nums
        cnt = Counter(nums)

        return heapq.nlargest(k, cnt.keys(), key=cnt.get)

    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums
        cnt = Counter(nums)

        keys = list(cnt.keys())
        start = 0
        end = len(keys)

        while k > 0:
            if start == end:
                return keys[:start+1]
            mid = random.randrange(start, end)
            print(start, end, mid, keys)

            keys[mid], keys[end-1] = keys[end-1], keys[mid]
            pter = start

            for i in range(start, end-1):
                if cnt[keys[i]] >= cnt[keys[end-1]]:
                    keys[i], keys[pter] = keys[pter], keys[i]
                    pter += 1
            keys[end-1], keys[pter] = keys[pter], keys[end-1]
            print(start, end, mid, pter, keys)

            if pter-start+1 == k:
                return keys[:pter+1]
            elif pter-start+1 < k:
                k -= pter-start+1
                start = pter + 1
            else:
                end = pter

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([3,0,1,0], 1))




