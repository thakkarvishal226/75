class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1

if __name__ == "__main__":
    s = Solution()
    nums = [0,1,0,3,12]
    print(s.moveZeroes(nums))
    print(nums)