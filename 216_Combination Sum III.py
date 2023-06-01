class Solution:
    def combinationSum3(self, k: int, n: int):
        if k > n:    # if number of elements greater than sum no point in checking
            return []
        if n > 45:   # we can have max sum 45 for [1,2....,9]
            return []
     
        lst = range(1,10)

        ans=[]

        def solve(ind, ds, target):
            if target == 0 and len(ds) == k: 
                ans.append(ds[:])     # have to append a copy to our final answer (i.e. we cannot do ans.append(ds))
                return 

            for i in range(ind,len(lst)):
                if target < lst[i]:
                    break
                ds.append(lst[i])      # add the element to our data structure
                solve(i+1, ds, target-lst[i])   # remove that element from target
                ds.pop()        # now during backtracking we have to remove that element from our data structure
        solve(0,[],n)
        return ans
                    

            
            
            

