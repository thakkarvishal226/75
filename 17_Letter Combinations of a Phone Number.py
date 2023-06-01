class Solution:
    def letterCombinations(self, digits: str):
        result = []
        ans = ""
        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def backtrack(i,ans):
            if i == len(digits):
                result.append(ans)
                return
            curr = mapping[digits[i]]
            for c in curr:
                ans = ans + c
                backtrack(i+1,ans)
                ans = ans[:len(ans)-1]
        backtrack(0,ans)
        return result

if __name__ == "__main__":
    obj = Solution()
    print(obj.letterCombinations("23"))