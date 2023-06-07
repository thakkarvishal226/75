from collections import deque

import unittest

class Solution:
    def orangesRotting(self, grid) -> int:
        q = deque()

        fresh, time = 0, 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        directions = [[1, 0],[0, 1],[-1, 0],[0, -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = dr+r
                    col = dc +c
                    if row < 0 or row == ROWS or col < 0  or col == COLS or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1


class TestCase(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()

    def test_case1(self):
        return self.assertEqual(self.obj.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]),4, "Issue In Logic Answer Not matching")

    def test_case2(self):
        return self.assertEqual(self.obj.orangesRotting([[0,2]]),0, "Issue In Logic Answer Not matching")
    

if __name__ == "__main__":
    unittest.main()