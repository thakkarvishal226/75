class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        max_index = 0
        array = []
        for i in range(len(candies)):
            if candies[i] > candies[max_index]:
                max_index = i
        
        for i in range(len(candies)):
            if candies[i]+extraCandies >= candies[max_index]:
                array.append(True)
            else:
                array.append(False)
        return array




if __name__ == "__main__":
    candies = [2,3,5,1,3] 
    extraCandies = 3
    obj = Solution()
    print(obj.kidsWithCandies(candies,extraCandies))
