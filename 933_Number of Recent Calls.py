import unittest
class RecentCounter:

    def __init__(self):
        self.queue = []
        

    def ping(self, t: int) -> int:
        
        while self.queue and t - self.queue[0] > 3000:
            del self.queue[0]
        self.queue.append(t)
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)




class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = RecentCounter()
        return super().setUp()
    
    def test_case1(self):
        self.assertEqual(self.obj.ping(1),1,"Fail")

    def test_case2(self):
        self.obj.ping(1)
        self.assertEqual(self.obj.ping(2),2,"Fail")

    def test_case3(self):
        self.obj.ping(1)
        self.obj.ping(2)
        self.assertEqual(self.obj.ping(3001),3,"Fail")
    
    def test_case4(self):
        self.obj.ping(1)
        self.obj.ping(2)
        self.obj.ping(3001)
        self.assertEqual(self.obj.ping(3002),3,"FAIL")
    def test_case5(self):
        self.obj.ping(642)
        self.obj.ping(1849)
        self.obj.ping(4921)
        self.obj.ping(5936)
        self.assertEqual(self.obj.ping(5957),3,"FAIL")


if __name__ == "__main__":
    unittest.main()