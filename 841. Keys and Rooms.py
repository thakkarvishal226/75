import unittest

class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        pass
        





class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.canVisitAllRooms([[1],[2],[3],[]]),True,"Fail")

    def test_case2(self):
        self.assertEqual(self.obj.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]),False,"Fail")
    
    def test_case2(self):
        self.assertEqual(self.obj.predictPartyVictory("RRDRDDD"),"Radiant","Fail")

    
if __name__ == "__main__":
    unittest.main()