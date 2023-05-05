import unittest
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R,D = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            rTurn = R.popleft()
            dTurn = D.popleft()

            if rTurn < dTurn:
                R.append(rTurn+len(senate))
            else:
                D.append(dTurn+len(senate))
        return "Radiant" if R else "Dire"



class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.predictPartyVictory("RD"),"Radiant","Fail")

    def test_case2(self):
        self.assertEqual(self.obj.predictPartyVictory("RDD"),"Dire","Fail")
    
    def test_case2(self):
        self.assertEqual(self.obj.predictPartyVictory("RRDRDDD"),"Radiant","Fail")

    
if __name__ == "__main__":
    unittest.main()