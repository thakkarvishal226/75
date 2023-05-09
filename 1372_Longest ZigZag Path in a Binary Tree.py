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
    def longestZigZag(self, root: TreeNode) -> int:
        self.result = 0
        def DFS(node, current_max_path, direction):
            if node != None:
                self.result = max(self.result, current_max_path)
                if direction:
                    DFS(node.right , current_max_path + 1 , False)
                    DFS(node.left , 1 , True)
                else:
                    DFS(node.left , current_max_path + 1 , True)
                    DFS(node.right , 1 , False)
        if root.left:
            DFS(root.left , 1 , True)

        if root.right:
            DFS(root.right , 1 , False)
        return self.result




        
        




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