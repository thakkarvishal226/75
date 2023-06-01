class Solution:
    def tribonacci(self, n: int) -> int:
        mem = {}
        def seq(n):
            if n in mem.keys():
                return mem[n]
            if (n == 0 ) :
                return 0
            elif (n == 2 or n == 1) :
                return 1
            else:
                res = seq(n-1) + seq(n-2) + seq(n-3)
                mem[n] = res
                return res
        return seq(n)


if __name__ == "__main__":
    obj= Solution()
    print(obj.tribonacci(4))