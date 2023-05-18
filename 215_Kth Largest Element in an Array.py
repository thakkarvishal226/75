
import unittest
"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.
"""


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # Creating Heap
        heap = []
        def insertHeap(n):
            heap.append(n)
            temp = len(heap)//2
            while temp > 0:
                if heap[temp] < heap[-1]:
                    pass



        for num in nums:
            pass
    
    

class TestClass(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.obj = Solution()
    def setUp(self) -> None:
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.findKthLargest([3,2,1,5,6,4],2),5,"Fail")
    
    def test_case2(self):
        self.assertEqual(self.obj.findKthLargest([3,2,3,1,2,4,5,5,6],4),4,"Fail")
    

if __name__ == "__main__":
    unittest.main()