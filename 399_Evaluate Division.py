import unittest
from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries): 
        graph = defaultdict(dict)
        for (num,den), val in zip(equations,values):
            graph[num][den] = val
            graph[den][num] = 1 / val
        def dfs(x, y,visited):
            if x not in  graph or y not in graph:
                return -1
            if y in graph[x]:
                return graph[x][y]
            
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i,y,visited)
                    if temp == -1:
                        continue
                    else:
                        return graph[x][i] * temp
            return -1
        
        res = []
        for query in queries:
            res.append(dfs(query[0], query[1],set()))
        return res



class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]),[6.00000,0.50000,-1.00000,1.00000,-1.00000],"Fail")

    def test_case2(self):
        self.assertEqual(self.obj.calcEquation([["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]),[3.75000,0.40000,5.00000,0.20000],"Fail")
    
    def test_case2(self):
        self.assertEqual(self.obj.calcEquation([["a","b"]],[0.5],[["a","b"],["b","a"],["a","c"],["x","y"]]),[0.50000,2.00000,-1.00000,-1.00000],"Fail")

    
if __name__ == "__main__":
    obj= Solution()
    obj.calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    unittest.main()