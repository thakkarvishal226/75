class Solution:
    def maxProfit(self, prices, fee: int) -> int: 
        EBP = prices[0]
        profit = 0
        TF = 2

        for i in prices[1:]:
            profit = max(profit,(i-EBP)-TF)
            EBP = min(EBP, i- profit)
        
        return profit
    


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxProfit([1,3,7,5,10,3],2))