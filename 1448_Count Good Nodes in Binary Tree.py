import unittest
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
    def goodNodes(self, root: TreeNode) -> int:
        if root:
            count = [0]
            def dfs(node,currMax):
                if not node: return

                if node.val >= currMax:
                    currMax = node.val
                    count[0] += 1
                if node.left:
                    dfs(node.left,currMax)
                
                if node.right:
                    dfs(node.right,currMax)
            dfs(root,root.val)
            return count[0]






class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        Tree1 = TreeNode(3,TreeNode(1,TreeNode(3)),TreeNode(4,TreeNode(1),TreeNode(5)))
        self.assertEqual(self.obj.goodNodes(Tree1),4,"Fail")

    def test_case2(self):
        Tree1 = TreeNode(1,TreeNode(3,TreeNode(4),TreeNode(2)))
        self.assertEqual(self.obj.goodNodes(Tree1),3,"Fail")

    def test_case3(self):
        Tree1 = TreeNode(1)
        self.assertEqual(self.obj.goodNodes(Tree1),1,"Fail")


if __name__ == "__main__":
    unittest.main()