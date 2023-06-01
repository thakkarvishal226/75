class Solution:
    def countBits(self, n: int):
        arr = []
        for i in range(n+1):
            count = 0
            _str = str(bin(i))[2:]
            for c in _str:
                if c  == '1':
                    count += 1
            arr.append(count)
        return arr


if __name__ == "__main__":
    obj = Solution()
    print(obj.countBits(5))