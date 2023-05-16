import unittest
from collections import defaultdict,deque
class Solution:
    def nearestExit(self, maze, entrance) -> int:
        m,n = len(maze),len(maze[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        q = deque([[entrance[0],entrance[1],0]])
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            xo,yo,steps = q.popleft()
            if (0 in [xo,yo] or xo==m-1 or yo==n-1) and [xo,yo]!=entrance:
                return steps
            for xn,yn in directions:
                x,y = xo+xn,yo+yn
                if 0<=x<m and 0<=y<n and maze[x][y]=='.':
                    maze[x][y] = '+'
                    q.append([x,y,steps+1])
        return -1



class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],[1,2]),1,"Fail")

    def test_case2(self):
        self.assertEqual(self.obj.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]],[1,0]),2,"Fail")
    
    def test_case3(self):
        self.assertEqual(self.obj.nearestExit([[".","+"]],[0, 0]),-1,"Fail")

    
if __name__ == "__main__":
    obj  = Solution()
    obj.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],[1,2])
    unittest.main()
