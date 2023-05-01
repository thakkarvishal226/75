
class Solution:
    def maxOperations(self, nums, k: int) -> int:
        nums = sorted(nums)
        left,right = 0 ,len(nums)-1
        count = 0
        while left < right:
            if nums[left]+nums[right] == k:
                count += 1
                left+= 1
                right -= 1
            elif nums[left]+nums[right] > k:
                right -= 1
            else:
                left += 1
        return count



if __name__ == "__main__":
    obj = Solution()
    nums = [3,1,3,4,3]
    k = 6
    print(obj.maxOperations(nums,k))