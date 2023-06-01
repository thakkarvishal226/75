class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0

        def findpath(x,y):
            if x == m and n == y:
                count += 1
                return
            elif x > m or y > n:
                return
            else:
                findpath(x+1,y) 
                findpath(x,y+1)
            
        