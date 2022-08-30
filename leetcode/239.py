class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = []

        def append_stack(n):
            if not stack:
                stack.append(n)
            else:
                while stack and nums[n] > nums[stack[-1]]:
                    stack.pop(-1)
                stack.append(n)

        def pop_element(n):
            while stack and n >= stack[0]:
                stack.pop(0)

        res = []
        for idx in range(k):
            append_stack(idx)
        res.append(nums[stack[0]])
        for idx in range(k, len(nums)):
            # pop the element is very important
            pop_element(idx - k)
            append_stack(idx)
            res.append(nums[stack[0]])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))