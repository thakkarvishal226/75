import unittest

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        pass


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.predictPartyVictory("RD"),"Radiant","Fail")

    def test_case2(self):
        self.assertEqual(self.obj.predictPartyVictory("RDD"),"Dire","Fail")
    
    # def test_case2(self):
    #     self.assertEqual(self.obj.predictPartyVictory("RRDRDDD"),"Radiant","Fail")

    
if __name__ == "__main__":
    unittest.main()