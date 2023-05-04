import unittest
class Solution:
    def findDifference(self, nums1, nums2):
        memory = [[],[]]
        for i in range(max(len(nums1),len(nums2))):
            if i < len(nums1):
                if nums1[i] not in nums2 and nums1[i] not in memory[0]:
                    memory[0].append(nums1[i])
            if i < len(nums2):
                if nums2[i] not in nums1 and nums2[i] not in memory[1]:
                    memory[1].append(nums2[i])
        return memory

class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.findDifference([1,2,3], [2,4,6]),[[1,3],[4,6]], "Fail")

    def test_case2(self):
        self.assertEqual(self.obj.findDifference([1,2,3,3],[1,1,2,2]),[[3],[]],"Fail")
    


if __name__ == "__main__":
    unittest.main()