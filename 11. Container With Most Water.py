class Solution:
    def maxArea(self, height) -> int:
        left , right = 0, len(height)-1
        max_val = 0
        while left<=right:
            min_length = height[right] if height[right] < height[left] else height[left]
            print(min_length*(right-(left)))
            if min_length*(right-(left)) > max_val:
                max_val = min_length*(right-(left))
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_val

if __name__ == "__main__":
    obj = Solution()
    height = [2,3,4,5,18,17,6]
    print(obj.maxArea(height))