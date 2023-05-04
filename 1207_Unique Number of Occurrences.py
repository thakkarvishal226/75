import unittest



class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        memory = {}
        for num in arr:
            if str(num) in memory.keys():
                memory[str(num)] += 1
            else:
                memory[str(num)] = 1
        return len(set(memory.values())) == len(memory.values())
        




class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertTrue(self.obj.uniqueOccurrences([1,2,2,1,1,3]), "Fail")

    def test_case2(self):
        self.assertFalse(self.obj.uniqueOccurrences([1,2]), "Fail")
    
    def test_case3(self):
        self.assertTrue(self.obj.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]), "Fail")


if __name__ == "__main__":
    unittest.main()