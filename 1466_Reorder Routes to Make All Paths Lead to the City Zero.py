import unittest

from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections) -> int:
        self.res = 0    
        roads = set()
        graph = defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)
        def dfs(u, parent):
            self.res += (parent, u) in roads
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)    
        dfs(0, -1)
        return self.res



class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]]),3,"Fail")

    def test_case2(self):
        self.assertEqual(self.obj.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]),2,"Fail")
    
    def test_case3(self):
        self.assertEqual(self.obj.minReorder(3,[[1,0],[2,0]]),0,"Fail")

    
if __name__ == "__main__":
    unittest.main()