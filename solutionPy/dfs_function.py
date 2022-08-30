from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        res = 1
        @lru_cache(None)
        def dfs(row, col):
            cnt = 0
            if row > 0 and matrix[row][col] < matrix[row-1][col]:
                cnt = max(cnt, dfs(row-1, col))
            if col > 0 and matrix[row][col] < matrix[row][col-1]:
                cnt = max(cnt, dfs(row, col-1))
            if row < len(matrix) - 1 and matrix[row][col] < matrix[row+1][col]:
                cnt = max(cnt, dfs(row+1, col))
            if col < len(matrix[0]) - 1 and matrix[row][col] < matrix[row][col+1]:
                cnt = max(cnt, dfs(row, col+1))
            return cnt + 1

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                res = max(res, dfs(row, col))

        return res

if __name__ == '__main__':
    s = Solution()
    print (s.longestIncreasingPath( [[3]]))
