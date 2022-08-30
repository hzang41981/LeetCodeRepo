class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # [7, 1, 5, 3, 6, 4]
        # 0stock: 0 ,  0,  4,
        # 1stock: -7, -1, -5, 1,

        dp = [[0,0] for i in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[-1][0] if dp[-1][0] > 0 else 0

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([5]))