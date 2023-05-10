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
    def searchBST_recursion(self, root: TreeNode, val: int) -> TreeNode:

        def rec(root):
            if root:
                if root.val == val: return root
                elif root.val < val: return rec(root.right)
                return rec(root.left)
        
        return rec(root)
    def searchBST_stack(self, root: TreeNode, val: int) -> TreeNode:
        queue =[root] 
        while queue:
            node = queue.pop()
            if node.val == val:
                return val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return None



class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        Tree1 = TreeNode(4,TreeNode(2,TreeNode(1,TreeNode(3))),TreeNode(7))
        self.assertEqual(self.obj.searchBST(Tree1,2).val,2,"Fail")

    def test_case2(self):
        Tree1 = TreeNode(18,TreeNode(2),TreeNode(22,None,TreeNode(63)))
        self.assertEqual(self.obj.searchBST(Tree1,63),4,"Fail")

    # def test_case3(self):
    #     Tree1 = TreeNode(1)
    #     self.assertEqual(self.obj.longestZigZag(Tree1),1,"Fail")


if __name__ == "__main__":
    unittest.main()