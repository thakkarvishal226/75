
import unittest
import heapq
"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.
"""


class Heap:
    def __init__(self) -> None:
        self.heap = []
    
    def shiftup(self,n):
        parent = (n-1)//2
        while parent >= 0 and self.heap[parent] < self.heap[n]:
            self.heap[parent], self.heap[n] = self.heap[n], self.heap[parent]
            n = parent
            parent = (n-1) // 2
    def shiftdown(self,n):
        if n < len(self.heap):
            child = (2*n) + 1
            if child < len(self.heap):
                if self.heap[child+1] and self.heap[child+1] > self.heap[n]:
                    self.heap[child+1],self.heap[n] = self.heap[n], self.heap[child+1]
                    n = child+1
                elif self.heap[child] and  self.heap[child] > self.heap[n]:
                    self.heap[child],self.heap[n] = self.heap[n], self.heap[child]
                    n = child
    def push(self, val):
        self.heap.append(val)
        self.shiftup(len(self.heap)-1)

    def pop(self, n):
        n +=  1 if n == 0 else 0
        child = (2*n) + 1
        while (2*child) + 1  <= len(self.heap):
            child = (2*child) + 1
        if child+1 < len(self.heap) and self.heap[child+1]:
            child += 1
        temp = self.heap[n]
        self.heap[n], self.heap[child] = self.heap[child], None
        self.shiftdown(n)
        return temp


if __name__ == "__main__":
    h = []
    for i in [3,2,1,5,6,4]:
        heapq.heappush(h,i)
    heapq._heapify_max(h) 
    print(h)
    for i in range(2):
        t = heapq.heappop(h)
        heapq._heapify_max(h)
    print(t)





        
    
    

# class TestClass(unittest.TestCase):
#     def __init__(self, methodName: str = "runTest") -> None:
#         super().__init__(methodName)
#         self.obj = Solution()
#     def setUp(self) -> None:
#         return super().setUp()
    
#     def test_case1(self):
#         self.assertEqual(self.obj.findKthLargest([3,2,1,5,6,4],2),5,"Fail")
    
#     def test_case2(self):
#         self.assertEqual(self.obj.findKthLargest([3,2,3,1,2,4,5,5,6],4),4,"Fail")
    

# if __name__ == "__main__":
#     unittest.main()