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
        count =  (count //2)-1
        next = head
        while count > 0:
            next = next.next
            count -= 1
        if next.next:
            next.next = next.next.next
        else:
            return None
        return head
        







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
        head = ListNode(1,ListNode(3,ListNode(4,ListNode(7,ListNode(1,ListNode(2,ListNode(6)))))))
        head = ListNode(1)
        self.assertEqual(self.check_result(head,self.obj.deleteMiddle(head)),True,"Fail")



if __name__ == "__main__":
    unittest.main()