class Solution:
    def compress(self, chars) -> int:
        curr = chars[0]
        curr_count  = 0
        out = ""
        for i in chars:
            if i == curr:
                curr_count+=1
            else:
                out+=curr
                out+=str(curr_count) if curr_count > 1 else ''
                curr_count = 1
            curr = i
        out+=curr
        out+=str(curr_count) if curr_count > 1 else ''
        print(out)
        for i in range(len(out)):
            chars[i] =out[i]
        return len(out)


if __name__ == "__main__":
    obj = Solution()
    chars = ["a","a","b","b","c","c","c"]
    print(obj.compress(chars))
    print(chars)