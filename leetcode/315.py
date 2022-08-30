class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        min_n = min(nums)
        max_n = max(nums)
        size = max_n - min_n + 1
        tree = [0 for _ in range(2 * size)]

        def update(target):
            target = target - min_n + size
            tree[target] += 1
            while target > 1:
                tree[target >> 1] = tree[target] + tree[target ^ 1]
                target >>= 1
            print(tree)

        def query(target):
            target = target - min_n + size
            l = size
            r = target
            res = 0
            while l < r:
                if l & 1:
                    res += tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res += tree[r]
                l >>= 1
                r >>= 1
            return res

        ret = [0 for _ in range(len(nums))]
        for i in reversed(range(len(nums))):
            ret[i] = query(nums[i])
            update(nums[i])
        return ret


if __name__ == '__main__':
    S = Solution()
    print(S.countSmaller([5, 2, 6, 1]))
