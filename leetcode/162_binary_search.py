class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        upper_idx = len(nums) - 1
        start = 0
        end = upper_idx
        while start <= end:
            mid = start + (end-start)//2
            mid_pre = nums[mid-1] if mid > 0 else -float('inf')
            mid_next = nums[mid+1] if mid < upper_idx else -float('inf')
            if mid_pre < nums[mid] and nums[mid] > mid_next:
                return mid
            start_pre = nums[start-1] if start > 0 else -float('inf')
            end_next = nums[end+1] if end < upper_idx else -float('inf')
            if start == mid:
                if start_pre < nums[mid] and nums[mid] > nums[end]:
                    return mid
            if (nums[mid] > nums[start] and nums[mid] > mid_next) or (mid_pre > nums[mid] and mid_pre > nums[start]):
                end = mid - 1

