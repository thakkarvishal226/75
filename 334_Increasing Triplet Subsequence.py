class Solution:
    def increasingTriplet(self, nums) -> bool:
        i = j = float("inf")
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    nums = [5,4,3,2,1]
    print(s.increasingTriplet(nums))