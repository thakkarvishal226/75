import unittest


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
                



class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.decodeString("3[a]2[bc]"),"aaabcbc","Fail")

    def test_case2(self):
        self.assertEqual(self.obj.decodeString("3[a2[c]]"),"accaccacc","Fail")

    def test_case3(self):
        self.assertEqual(self.obj.decodeString("2[abc]3[cd]ef"),"abcabccdcdcdef","Fail")
    
    def test_case4(self):
        self.assertEqual(self.obj.decodeString("abc3[cd]xyz"),"abccdcdcdxyz","FAIL")
if __name__ == "__main__":
    unittest.main()