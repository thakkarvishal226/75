import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        def feasible(speed) -> bool:
            return sum(math.ceil(pile / speed) for pile in piles) <= h  # slower
            # return sum((pile - 1) / speed + 1 for pile in piles) <= h  # faster

        left, right = 1, max(piles)
        while left < right:
            mid = left  + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
    

if __name__ == "__main__":
    obj = Solution()
    print(obj.minEatingSpeed([3,6,7,11],8))