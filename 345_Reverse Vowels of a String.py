class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j = 0,len(s)-1
        vowel = "aeiouAEIOU"
        s = list(s)
        while i<j:
            if s[i] not in vowel:
                i += 1
            if s[j] not in vowel:
                j -= 1
            if s[i] in vowel and s[j] in vowel:
                temp = s[j]
                s[j] = s[i]
                s[i] = temp
                i+=1
                j-=1
        return "".join(s)



if __name__ == "__main__":
    obj = Solution()
    s = "aA"
    print(obj.reverseVowels(s))