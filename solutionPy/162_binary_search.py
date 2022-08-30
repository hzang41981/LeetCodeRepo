class Solution:
    def findPeakElement(self, nums) -> int:
        len_nums = len(nums)
        start = 0
        end = len_nums - 1

        while start <= end:
            mid = start + (end - start) // 2
            prev = nums[mid-1] if mid > 0 else -float('inf')
            nxt = nums[mid+1] if mid < len_nums - 1 else -float('inf')
            if prev < nums[mid] and nums[mid] > nxt:
                return mid

            before_start = nums[start-1] if start > 0 else -float('inf')
            after_end = nums[end + 1] if end < len_nums - 1 else -float('inf')
            if nums[mid] < nums[end] and nums[end] > after_end:
                start = mid + 1
            if nums[start] > nums[mid] and nums[start] > before_start:
                end = mid - 1
            print(start, end, mid)
if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([1,2,3,1]))