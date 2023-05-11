import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return f"{self.val}"
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        
        if root.val == key:
            if not root.right: return root.left
            
            if not root.left: return root.right
            
            if root.left and root.right:
                temp = root.right
                while temp.left: temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root




class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def check_Tree(self,root1,root2):
        queue = [[root1,root2]]
        while queue:
            q = queue.pop()
            if q[0] and (q[0] == q[1]):
                queue.append([q[0].left,q[1].left])
                queue.append([q[0].right,q[1].right])
            else:
                return False
        return True

    def test_case1(self):
        Tree1 = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(6,None,TreeNode(7)))
        Tree2 = TreeNode(5,TreeNode(4,TreeNode(2)),TreeNode(6,None,TreeNode(7)))
        self.assertEqual(self.check_Tree(self.obj.deleteNode(Tree1,6),Tree2),True,"Fail")

    # def test_case2(self):
    #     Tree1 = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(6,None,TreeNode(7)))
    #     Tree2 = TreeNode(5,TreeNode(4,TreeNode(2)),TreeNode(6,None,TreeNode(7)))
    #     self.assertEqual(self.check_Tree(self.obj.deleteNode(Tree1),Tree2),True,"Fail")

    # def test_case3(self):
    #     Tree1 = TreeNode(1)
    #     self.assertEqual(self.obj.longestZigZag(Tree1),1,"Fail")


if __name__ == "__main__":
    unittest.main()