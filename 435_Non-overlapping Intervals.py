import sys
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        result, prev = 0, -sys.maxsize
        for l, r in intervals:
            if l < prev:
                result += 1
                if r > prev:
                    continue
            prev = r
        return result

if __name__ == "__main__":
    obj = Solution()
    print(obj.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))