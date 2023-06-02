class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        for i in range(32):
            ai = False
            bi = False
            ci = False
            if (a & (1 << i)) > 0: ai =True
            if (b & (1 << i)) > 0: bi =True
            if (c & (1 << i)) > 0: ci =True

            if ci:
                if not ai and not bi:
                    cnt += 1
            else:
                if ai and bi:
                    cnt += 2
                elif ai or bi:
                    cnt += 1
        return cnt
                    


if __name__ == "__main__":
    obj = Solution()
    print(obj.minFlips(2,6,5))