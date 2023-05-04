import unittest

class Solution:
    def removeStars(self, s: str) -> str:
        stack =[]
        for i in range(len(s)):
            if s[i] == "*":
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.removeStars("leet**cod*e"),"lecoe","Fail")

    def test_case2(self):
        self.assertEqual(self.obj.removeStars("erase*****"),"","Fail")
    
    # def test_case3(self):
    #     self.assertEqual(self.obj.removeStars([[11,1],[1,11]]),2,"Fail")


    # def test_case4(self):
    #     self.assertEqual(self.obj.removeStars([[2,1],[1,34]]),2,"Fail")

if __name__ == "__main__":
    unittest.main()
    