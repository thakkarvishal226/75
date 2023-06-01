from math import ceil
class Solution:
    def successfulPairs(self, spells, potions, success: int):
        ans = []
        potions = sorted(potions)
        for i in spells:
            start , end = 0, len(potions)-1
            maxsucess_index = len(potions)
            while start <= end:
                mid = start + (end-start)//2

                if potions[mid] * i>= success:
                    maxsucess_index = mid
                    end = mid-1
                else:
                    start = mid+1
            ans.append(len(potions)-maxsucess_index)



        return ans
            
            
    


if __name__ == "__main__":
    obj = Solution()
    print(obj.successfulPairs([5,1,3],[1,2,3,4,5],7))