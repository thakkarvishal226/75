import unittest
from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        q = deque([[0,0,0]])
        fresh = 0
        while q:
            xo, yo, step = q.popleft()
            if (xo==m-1 and yo==n-1 and fresh == 0):
                for i in grid:
                    if 1 in i:
                        return -1
                return step
            if grid[xo][yo] == 2:
                for xn,yn in directions:
                    x,y = xo+xn,yo+yn
                    if 0<=x<m and 0<=y<n and grid[x][y] ==1:
                        grid[x][y] = 2
                        fresh -= 1 if fresh > 0 else 0
                        q.append([x,y,step+1])
            else:
                if grid[xo][yo] == 1:
                    fresh += 1
                for xn,yn in directions:
                    x,y = xo+xn,yo+yn
                    if 0<=x<m and 0<=y<n:
                        q.append([x,y,step])


        return step


# Time complexity: O(rows * cols) -> each cell is visited at least once
# Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue

# class Solution:
#     def orangesRotting(self, grid) -> int:
        
#         # number of rows
#         rows = len(grid)
#         if rows == 0:  # check if grid is empty
#             return -1
        
#         # number of columns
#         cols = len(grid[0])
        
#         # keep track of fresh oranges
#         fresh_cnt = 0
        
#         # queue with rotten oranges (for BFS)
#         rotten = deque()
        
#         # visit each cell in the grid
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 2:
#                     # add the rotten orange coordinates to the queue
#                     rotten.append((r, c))
#                 elif grid[r][c] == 1:
#                     # update fresh oranges count
#                     fresh_cnt += 1
        
#         # keep track of minutes passed.
#         minutes_passed = 0
        
#         # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
#         while rotten and fresh_cnt > 0:

#             # update the number of minutes passed
#             # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
#             minutes_passed += 1
            
#             # process rotten oranges on the current level
#             for _ in range(len(rotten)):
#                 x, y = rotten.popleft()
                
#                 # visit all the adjacent cells
#                 for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
#                     # calculate the coordinates of the adjacent cell
#                     xx, yy = x + dx, y + dy
#                     # ignore the cell if it is out of the grid boundary
#                     if xx < 0 or xx == rows or yy < 0 or yy == cols:
#                         continue
#                     # ignore the cell if it is empty '0' or visited before '2'
#                     if grid[xx][yy] == 0 or grid[xx][yy] == 2:
#                         continue
                        
#                     # update the fresh oranges count
#                     fresh_cnt -= 1
                    
#                     # mark the current fresh orange as rotten
#                     grid[xx][yy] = 2
                    
#                     # add the current rotten to the queue
#                     rotten.append((xx, yy))

        
#         # return the number of minutes taken to make all the fresh oranges to be rotten
#         # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
#         return minutes_passed if fresh_cnt == 0 else -1







class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]),4,"Fail")

    def test_case2(self):
        self.assertEqual(self.obj.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]),-1,"Fail")
    
    def test_case3(self):
        self.assertEqual(self.obj.orangesRotting([[1,2]]),0,"Fail")

    
if __name__ == "__main__":
    #obj  = Solution()
    #obj.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],[1,2])
    unittest.main()