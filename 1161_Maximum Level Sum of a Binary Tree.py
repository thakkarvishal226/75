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
    def maxLevelSum(self, root) -> int:
        queue = [root]
        maxsum = float("-inf")
        count = 1
        maxlevel = 1
        while queue:
            t = queue.copy()
            queue.clear()
            sum = 0
            for i in t:
                sum += i.val
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            if maxsum < sum:
                maxsum = sum
                maxlevel = count
            count+=1
        return maxlevel
            

    






class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def check_result(self,input,output):
        node1 = input
        node2 = output
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True if not (node1 and node2) else False
    
    def test_case1(self):
        root = TreeNode(1,TreeNode(7,TreeNode(7),TreeNode(-8)),TreeNode(0))
        self.assertEqual(self.obj.maxLevelSum(root),2,"Fail")

    def test_case2(self):
        root = TreeNode(-100,TreeNode(-200,TreeNode(-20),TreeNode(-5)),TreeNode(-300,TreeNode(-10)))
        self.assertEqual(self.obj.maxLevelSum(root),3,"Fail")

if __name__ == "__main__":
    unittest.main()
