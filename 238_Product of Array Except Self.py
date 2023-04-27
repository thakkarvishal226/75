class Solution:
    def productExceptSelf(self, nums):
        extra = 1
        length = len(nums)
        out = [1]*length
        for i in range(length):
            out[i] *= extra
            extra *= nums[i]
        extra = 1
        for i in range(length-1,-1,-1):
            out[i] *= extra
            extra *= nums[i]
        return out



if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4]
    print(s.productExceptSelf(nums))