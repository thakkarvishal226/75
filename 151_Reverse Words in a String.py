class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = [word.strip() for word in words if len(word)>0]
        return " ".join(words[::-1])


if __name__ == "__main__":
    s = "a good   example"
    obj = Solution()
    print(obj.reverseWords(s))
