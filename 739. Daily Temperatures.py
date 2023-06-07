class Solution:
    def dailyTemperatures(self, temperatures):
        res =[0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            stack.append([t, i])
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.dailyTemperatures([73,74,75,71,69,72,76,73]))