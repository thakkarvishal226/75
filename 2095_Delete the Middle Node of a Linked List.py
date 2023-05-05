import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        next =head
        count = 0
        while next:
            next = next.next
            count+=1
        count = count //2
        next = head
        while count > 0:
            next = next.next
            count -= 1
        next.next = next.next.next
        return head
        







class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.deleteMiddle("3[a]2[bc]"),"aaabcbc","Fail")



if __name__ == "__main__":
    unittest.main()