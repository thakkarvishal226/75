class Solution:
    def findPeakElement(self, nums) -> int:
        if(len(nums) == 1): 
              return 0; # single element
        n = len(nums)
        
        # check if 0th/n-1th index is the peak element
        if(nums[0] > nums[1]):
             return 0
        if(nums[n-1] > nums[n-2]):
            return n-1
		
		# search in the remaining array
        start = 1
        end = n-2
        
        while(start <= end):
            mid = start + (end - start)//2
            if(nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]):
                return mid
            elif(nums[mid] < nums[mid-1]):
                end = mid - 1
            elif(nums[mid] < nums[mid+1]):
                start = mid + 1
        
        return -1; # dummy return statement

if __name__ == "__main__":
    obj = Solution()
    print(obj.findPeakElement([1,2,1,3,5,6,4]))