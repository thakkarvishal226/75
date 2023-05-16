import unittest
class Solution:
    def findCircleNum(self, A):
        N = len(A)
        seen = set()
        def dfs(node):
            for nei, adj in enumerate(A[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans




class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]),2,"Fail")

    def test_case2(self):
        self.assertEqual(self.obj.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]),3,"Fail")
    

    
if __name__ == "__main__":
    unittest.main()