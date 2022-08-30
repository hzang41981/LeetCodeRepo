from collections import defaultdict
class Solution(object):
    def longestSubstring2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def dc(start, end):
            cnt = [0 for _ in range(26)]
            for i in range(start, end):
                cnt[ord(s[i])-ord("a")] += 1
            for i in range(start, end):
                if cnt[ord(s[i])-ord("a")] < k:
                    return max(dc(start, i), dc(i + 1, end))
            return end - start

        return dc(0, len(s))

    def longestSubstring(self, s: str, k: int) -> int:
        cnt = [0 for _ in range(26)]
        max_len = 0
        len_s = len(s)
        for c in s:
            cnt[ord(c)-ord('a')] += 1
        for count in cnt:
            if count >= k:
                max_len += 1
        res = 0
        for m in range(1, max_len+1):
            num_meet = 0
            num_c = 0
            start = 0
            end = 0
            count = [0 for _ in range(26)]
            while end < len_s:
                if num_c <= m:
                    if count[ord(s[end])-ord('a')] == 0:
                        num_c += 1
                    count[ord(s[end])-ord('a')] += 1
                    if count[ord(s[end])-ord('a')] == k:
                        num_meet += 1
                    if num_c == num_meet and num_meet == m:
                        res = max(res, end-start+1)
                    end += 1
                else:
                    if count[ord(s[start])-ord('a')] == 1:
                        num_c -= 1
                    count[ord(s[start]) - ord('a')] -= 1
                    if count[ord(s[start]) - ord('a')] == k-1:
                        num_meet -= 1
                    if num_c == num_meet and num_meet == m:
                        res = max(res, end-start+1)
                    start += 1

        return res



if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring("aaaccbdcabb", 3))
