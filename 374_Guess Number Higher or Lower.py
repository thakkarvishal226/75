# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0


class Solution:
    def __init__(self,n) -> None:
        self.geuss_num = n 
    def guessNumber(self, n: int) -> int:
        start,mid = 0, n // 2
        if start == mid:
            return n
        while start < n:
            if self.guess(mid) == -1:
                n = mid
            elif self.guess(mid) == 1:
                start = mid
            else:
                return mid
            if (start + n) % 2 == 0:
                mid =  (start + n) // 2
            else:
                mid =  (start + n+1) // 2
            
    def guess(self,num: int) -> int:
        if num == self.geuss_num:
            return 0
        if num < self.geuss_num:
            return 1
        if num > self.geuss_num:
            return -1
    
    
if __name__ == "__main__":
    obj = Solution(2)
    print(obj.guessNumber(2))