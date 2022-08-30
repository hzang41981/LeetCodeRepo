from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def divide(start, end):
            if start >= end:
                return 0
            cnt_s = Counter(s[start:end])
            for idx in range(start, end):
                if cnt_s[s[idx]] < k:
                    first_end = idx
                    while idx < len(s) and cnt_s[s[idx]] < k:
                        idx += 1
                    return max(divide(start, first_end), divide(idx, end))
            return end-start
        return divide(0, len(s))

if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring("aaabb", 3))