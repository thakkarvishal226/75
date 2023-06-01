class Solution:
    def numTilings(self, n: int) -> int:
        mod = 1e9 + 7
        dp = {}
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4,n+1):
            dp[i] = ((2 * dp[i-1]) + dp[i-3]) % mod
        return dp[n]
    


if __name__ == "__main__":
    obj = Solution()
    print(obj.numTilings(5))