import unittest
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertTrue(self.obj.closeStrings("abc","bca"),"Fail")

    def test_case2(self):
        self.assertFalse(self.obj.closeStrings("a","aa"),"Fail")
    
    def test_case3(self):
        self.assertTrue(self.obj.closeStrings("cabbba","abbccc"),"Fail")


    def test_case4(self):
        self.assertFalse(self.obj.closeStrings("abbbzcf","babzzcz"),"Fail")

    def test_case5(self):
        self.assertFalse(self.obj.closeStrings("abbzzca","babzzcz"),"Fail")
if __name__ == "__main__":
    unittest.main()


