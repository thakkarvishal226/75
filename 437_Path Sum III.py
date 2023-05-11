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
         # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, targetSum, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1




class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        Tree1 = TreeNode(10,TreeNode(5,TreeNode(3,TreeNode(3),TreeNode(-1)),TreeNode(2,None,TreeNode(1))),TreeNode(-3,None,TreeNode(11)))
        self.assertEqual(self.obj.pathSum(Tree1,8),3,"Fail")

    # def test_case2(self):
    #     Tree1 = TreeNode(1,TreeNode(1,None,TreeNode(1,TreeNode(1,None,TreeNode(1)),TreeNode(1))),TreeNode(1))
    #     self.assertEqual(self.obj.longestZigZag(Tree1),4,"Fail")

    # def test_case3(self):
    #     Tree1 = TreeNode(1)
    #     self.assertEqual(self.obj.longestZigZag(Tree1),1,"Fail")


if __name__ == "__main__":
    unittest.main()