class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        s = sum(nums[:k])
        mymax = s
        for i in range(1,len(nums)-k+1):
            s = (s - nums[i-1] + nums[k+i-1])
            mymax = max(s,mymax)
        return mymax/k




if __name__ == "__main__":
    nums = [0,4,0,3,2]
    k = 1
    obj = Solution()
    print(obj.findMaxAverage(nums,k))
