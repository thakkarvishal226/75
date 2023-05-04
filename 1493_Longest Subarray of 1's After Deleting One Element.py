class Solution:
    def longestSubarray(self, nums) -> int:
        j = 0
        max_len = 0
        cnt = 1
        for i in range(len(nums)):
            if (nums[i] == 0):
                cnt -= 1
            if cnt < 0:
                if nums[j] == 0:
                    cnt += 1
                    max_len = max(max_len,(i-j))
                j+=1
        if cnt == 1:
            return len(nums) - 1
        return max_len if cnt > 0  else (i-j)



if __name__ == "__main__":
    nums = [1,1,0,1]
    nums = [0,0,0]
    #nums = [0,1,1,1,0,1,1,0,1]
    #nums = [1,1,0,0,1,1,1,0,1]
    obj = Solution()
    print(obj.longestSubarray(nums))
