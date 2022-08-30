class Solution:
    def kthSmallest(self, matrix: list, k: int) -> int:
        len_c = len(matrix[0])
        len_r = len(matrix)
        def cnt(m):
            res = 0
            max_element = -float('inf')
            cnt_m = 0
            for col in range(len_c):
                for row in range(len_r-1, -1, -1):
                    if matrix[row][col] == m:
                        cnt_m += 1
                        res += 1
                        max_element = max(max_element, matrix[row][col])
                    elif matrix[row][col] < m:
                        res += (row + 1)
                        max_element = max(max_element, matrix[row][col])
                        #important
                        break
            return res, max_element, cnt_m
        start = matrix[0][0]
        end = matrix[-1][-1]
        while start < end:
            mid = start + (end-start)//2
            less_or_equal, max_e, cnt_m = cnt(mid)
            # important
            if less_or_equal == k:
                return max_e
            elif less_or_equal < k:
                start = mid + 1
            elif less_or_equal - cnt_m < k < less_or_equal:
                return mid
            else:
                end = mid - 1

        return start

if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest([[2,3,6,6,10],
                         [5,9,12,17,19],
                         [10,14,17,20,20],
                         [15,17,20,24,24],
                         [20,20,25,26,29]], 4))