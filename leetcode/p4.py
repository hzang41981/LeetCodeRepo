class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def findKSamllest(p1, p2, k):
            if p1 == len(nums1):
                return nums2[p2 + k - 1]
            if p2 == len(nums2):
                return nums1[p1 + k - 1]
            if k == 1:
                return min(nums1[p1], nums2[p2])
            m1 = p1 + k//2 - 1 if p1 + k//2 - 1 < len(nums1) else len(nums1) - 1
            m2 = p2 + k//2 - 1 if p2 + k//2 - 1 < len(nums2) else len(nums2) - 1

            if nums1[m1] <= nums2[m2]:
                m1 += 1
                return findKSamllest(m1, p2, k-(m1-p1))
            else:
                m2 += 1
                return findKSamllest(p1, m2, k-(m2-p2))

        if (len(nums1) + len(nums2)) % 2 == 0:
            return (findKSamllest(0,0, (len(nums1) + len(nums2)) // 2) + findKSamllest(0,0, (len(nums1) + len(nums2)) // 2 + 1)) / 2
        else:
            return findKSamllest(0,0, (len(nums1) + len(nums2)) // 2 + 1)

    # p10
    # TODO
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[0 for _ in range(len(p)) for _ in range(len(s))]]
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == "*":
                    if p[j-1] == s[i]:
                        dp[i][j] = max(dp[i][j-2], dp[i-1][j])
                    else:
                        dp[i][j] = dp[i][j-2]
                else:
                    if p[j] == s[i]:
                        dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print (s.findMedianSortedArrays([2],[1,3]))