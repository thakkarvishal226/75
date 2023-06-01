class Solution:
    def singleNumber(self, nums) -> int:
        res = 0

        for i in nums:
            res = i ^ res
        return res
    

if __name__ == "__main__":
    obj = Solution()
    print(obj.singleNumber([4,1,2,1,2]))