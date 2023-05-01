class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        size = k // 2
        avg = 0
        max = float("-inf")
        if len(nums) == 1:
            return nums[0]
        for i in range(size,len(nums)-size+1):
            avg = sum(nums[i-size:i+(size if size>0 else 1)+1])/k
            max = avg if avg > max else max
        return max


if __name__ == "__main__":
    nums = [3,3,4,3,0]
    k = 3
    obj = Solution()
    print(obj.findMaxAverage(nums,k))
