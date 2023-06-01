import heapq
"""
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.
"""

class Solution:
    def totalCost(self, costs, k: int, candidates: int) -> int:
        output = 0
        heap = []
        
        l, r = 0, len(costs) - 1
        j = candidates
        while l <= r and j:
            heapq.heappush(heap, (costs[l], l))
            # If l and r point to the same cell in costs don't push it twice
            if l != r:
                heapq.heappush(heap, (costs[r], r))
            l += 1
            r -= 1
            j -= 1

        while k:
            val, idx = heapq.heappop(heap)
            output += val
            if l <= r:
                # After every hire a new spot in the hiring pool opens we need to fill
                # We must figure out if the last candidate that was popped was from the left side
                # or the right side
                if abs(idx - l) <= abs(idx - r):
                    heapq.heappush(heap, (costs[l], l))
                    l += 1
                else:
                    heapq.heappush(heap, (costs[r], r))
                    r -= 1
        
            k -= 1
            
        
        return output 
            


if __name__ == "__main__":
    obj = Solution()
    print(obj.totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58],11,2))
        
