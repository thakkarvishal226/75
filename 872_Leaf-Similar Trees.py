import unittest
import itertools
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return f"{self.val}"

    def __repr__(self) -> str:
        return f"{self.val}"

class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
            for i in dfs(node.left):
                yield i
            for i in dfs(node.right):
                yield i
        result = [a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2))]
        return all(result)








class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        Tree1 = TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),TreeNode(1,TreeNode(9),TreeNode(8)))
        Tree2 = TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(7)),TreeNode(1,TreeNode(4),TreeNode(2,TreeNode(9),TreeNode(8))))
        self.assertEqual(self.obj.leafSimilar(Tree1,Tree2),True,"Fail")

    def test_case2(self):
        Tree1 = TreeNode(1,TreeNode(2),TreeNode(3))
        Tree2 = TreeNode(1,TreeNode(3),TreeNode(2))
        self.assertEqual(self.obj.leafSimilar(Tree1,Tree2),False,"Fail")

    def test_case3(self):
        Tree1 = TreeNode(1,TreeNode(2))
        Tree2 = TreeNode(2,TreeNode(2))
        self.assertEqual(self.obj.leafSimilar(Tree1,Tree2),True,"Fail")

def square(n):
    h = 10
    hh = [10,20,30406,2352,523,5,235,2354]
    for i in range(n):
        yield i*i

if __name__ == "__main__":
    unittest.main()