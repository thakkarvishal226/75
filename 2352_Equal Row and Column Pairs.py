import unittest
class Solution:
    def equalPairs(self, grid) -> int:
        j = len(grid)
        count = 0
        my_map1 = []
        my_map2 = []
        if len(grid) == 2:
            if (grid[0][0] - grid[1][1]) ==0 and (grid[0][1] - grid[1][0]) == 0:
                return 2
        for i in range(j):
            my_map1.append(grid[i][i])
            my_map2.append(grid[i][j-i-1])
        my_map1= sorted(my_map1)
        my_map2= sorted(my_map2)
        for i,j in zip(my_map1,my_map2):
            if i == j:
                count+=1
        return count

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