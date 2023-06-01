class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))

        for i in range(2,len(nums)):
            dp.append(max(dp[i-2] + nums[i],dp[i-1]))
        return dp[-1]
            


if __name__ == "__main__":
    obj = Solution()
    print(obj.rob([2,7,9,3,1]))