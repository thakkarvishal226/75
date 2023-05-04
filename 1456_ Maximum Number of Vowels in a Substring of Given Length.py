class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowel = "aeiou"
        for i in range(0,k):
            if s[i] in vowel:
                count+=1
        max_cnt = count
        for i in range(1,len(s)-k+1):
            if s[i-1] in vowel:
                count -= 1
            if s[i+k-1] in vowel:
                count += 1
            max_cnt = max(count,max_cnt)
        return max_cnt


if __name__ == "__main__":
    s = "weallloveyou"
    k = 7
    obj = Solution()
    print(obj.maxVowels(s,k))