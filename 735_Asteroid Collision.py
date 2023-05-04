import unittest
class Solution:
    def asteroidCollision(self, asteroids):
        s = []
        for a in asteroids:
            while s and s[-1] > 0 and a < 0:
                if s[-1] + a < 0: s.pop()
                elif s[-1] + a > 0: break    
                else: s.pop(); break
            else: s.append(a)        
        return s



class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.asteroidCollision([5,10,-5]),[5,10],"Fail")

    def test_case2(self):
        self.assertEqual(self.obj.asteroidCollision([8,-8]),[],"Fail")
    
    def test_case3(self):
        self.assertEqual(self.obj.asteroidCollision([-8,8]),[-8,8],"Fail")


    def test_case4(self):
        self.assertEqual(self.obj.asteroidCollision([10,2,-5]),[10],"Fail")

    def test_case5(self):
        self.assertEqual(self.obj.asteroidCollision([-2,-1,1,2]),[-2,-1,1,2],"Fail")

    def test_case6(self):
        self.assertEqual(self.obj.asteroidCollision([-2,1,-2,-1]),[-2,-2,-1])
    
    def test_case7(self):
        self.assertEqual(self.obj.asteroidCollision([-2,1,-1,-2]),[-2,-2],"Fail")

if __name__ == "__main__":
    unittest.main()
    
