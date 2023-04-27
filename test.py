class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i,j = 0, len(s)-1
        while i <= j:
            print(i,j)
            temp = s[i]
            s[i] = s[j]
            s[j]=temp
            i+=1
            j-=1
        

if __name__  == "__main__":
    s = ["h","e","l","l","o","y"]
    obj = Solution()
    obj.reverseString(s)
    print(s)