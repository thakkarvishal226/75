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
    def rightSideView(self, root: TreeNode):
        queue = [root] if root else []
        right_value = []
        while queue:
            t = queue.copy()
            queue.clear()
            for i in t:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            right_value.append(i.val)
        return right_value

                






class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        Tree1 = TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3,None,TreeNode(4)))
        self.assertEqual(self.obj.rightSideView(Tree1),[1,3,4],"Fail")

    def test_case2(self):
        Tree1 = TreeNode(18,TreeNode(2),TreeNode(22,None,TreeNode(63)))
        self.assertEqual(self.obj.rightSideView(Tree1),[18,22,63],"Fail")

    def test_case3(self):
        Tree1 = TreeNode(1,None,TreeNode(3))
        self.assertEqual(self.obj.rightSideView(Tree1),[1,3],"Fail")

    def test_case3(self):
            Tree1 = None
            self.assertEqual(self.obj.rightSideView(None),[],"Fail")

if __name__ == "__main__":
    unittest.main()
    