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
    def pathSum(self, root:TreeNode, targetSum: int) -> int:
        pass
    




class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        Tree1 = TreeNode(1,None,TreeNode(1,TreeNode(1),TreeNode(1,TreeNode(1,None,TreeNode(1,None,TreeNode(1))),TreeNode(1))))
        self.assertEqual(self.obj.longestZigZag(Tree1),3,"Fail")

    def test_case2(self):
        Tree1 = TreeNode(1,TreeNode(1,None,TreeNode(1,TreeNode(1,None,TreeNode(1)),TreeNode(1))),TreeNode(1))
        self.assertEqual(self.obj.longestZigZag(Tree1),4,"Fail")

    # def test_case3(self):
    #     Tree1 = TreeNode(1)
    #     self.assertEqual(self.obj.longestZigZag(Tree1),1,"Fail")


if __name__ == "__main__":
    unittest.main()