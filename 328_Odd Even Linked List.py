import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        odd_head = None
        even_head = None
        odd_next = odd_head
        even_next = even_head
        index = 1
        while head:
            if index % 2 == 0:
                if not even_head:
                    even_head = ListNode(head.val)
                    even_next = even_head
                else:
                    even_next.next = ListNode(head.val)
                    even_next = even_next.next
            else:
                if not odd_head:
                    odd_head = ListNode(head.val)
                    odd_next = odd_head
                else:
                    odd_next.next = ListNode(head.val)
                    odd_next = odd_next.next
            head = head.next
            index += 1
        if odd_head:
            odd_next.next = even_head
        return odd_head




class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def check_result(self,input,output):
        node1 = input
        node2 = output
        count = -1
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
            count+=1
        return True if not (node1 and node2) and count > 0 else False
    
    def test_case1(self):
        head = ListNode(1,ListNode(3,ListNode(4,ListNode(7,ListNode(2,ListNode(6))))))
        head_out = ListNode(1,ListNode(3,ListNode(7,ListNode(4,ListNode(2,ListNode(6))))))
        self.assertEqual(self.check_result(head_out,self.obj.oddEvenList(head)),True,"Fail")



if __name__ == "__main__":
    unittest.main()