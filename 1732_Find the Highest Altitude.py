import unittest
class Solution:
    def largestAltitude(self, gain) -> int:
        max_altitute = 0
        curr_alltitute = 0 
        for num in gain:
            curr_alltitute += num
            max_altitute = max(max_altitute,curr_alltitute)
        return max_altitute

class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.largestAltitude([-5,1,5,0,-7]),1,"Fail")

    def test_case2(self):
        self.assertEqual(self.obj.largestAltitude([-4,-3,-2,-1,4,3,2]),0,"Fail")
    
        

if __name__ == "__main__":
    unittest.main()