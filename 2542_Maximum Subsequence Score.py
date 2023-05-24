from heapq import heappop,heappush
"""
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.
"""
from itertools import permutations,combinations
class Solution:
    def maxScore(self, nums1, nums2, k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1,nums2)]
        pairs = sorted(pairs,key= lambda x: x[1],reverse=True)
        n1Sum = 0
        res = 0
        minHeap = []
        for n1, n2 in pairs:
            n1Sum += n1
            heappush(minHeap, n1)
            if len(minHeap) > k:
                n1Sum -= heappop(minHeap)

            if len(minHeap) == k:
                res = max(res, n1Sum * n2)
        return res


        


if __name__ == "__main__":
    obj = Solution()
    num1 = [93,463,179,2488,619,2006,1561,137,53,1765,2304,1459,1768,450,1938,2054,466,331,670,1830,1550,1534,2164,1280,2277,2312,1509,867,2223,1482,2379,1032,359,1746,966,232,67,1203,2474,944,1740,1775,1799,1156,1982,1416,511,1167,1334,2344]
    num2 = [345,229,976,2086,567,726,1640,2451,1829,77,1631,306,2032,2497,551,2005,2009,1855,1685,729,2498,2204,588,474,693,30,2051,1126,1293,1378,1693,1995,2188,1284,1414,1618,2005,1005,1890,30,895,155,526,682,2454,278,999,1417,1682,995]

    print(obj.maxScore(num1,num2,3))