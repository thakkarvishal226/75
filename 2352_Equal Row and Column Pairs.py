import unittest
from collections import defaultdict
import numpy as np

class Solution:
    def equalPairs(self, grid) -> int:
        row_hash = defaultdict(dict)

        for i in grid:
            row_ = "#".join([str(j) for j in i ])
            if not row_ in row_hash.keys():
                row_hash[row_] = 1
            else:
                row_hash[row_]  += 1
        ans = 0
        for col in zip(*grid):
            col_ = "#".join([str(j) for j in col ])
            if col_ in row_hash.keys():
                ans += row_hash[col_]
        return ans



        
        
        

        #print(my_map)




class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.equalPairs([[3,2,1],[1,7,6],[2,7,7]]),1,"Fail")

    def test_case2(self):
        self.assertEqual(self.obj.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]),3,"Fail")
    
    def test_case3(self):
        self.assertEqual(self.obj.equalPairs([[11,1],[1,11]]),2,"Fail")


    def test_case4(self):
        self.assertEqual(self.obj.equalPairs([[2,1],[1,34]]),2,"Fail")

    # def test_case5(self):
    #     self.assertFalse(self.obj.closeStrings("abbzzca","babzzcz"),"Fail")



if __name__ == "__main__":
    unittest.main()