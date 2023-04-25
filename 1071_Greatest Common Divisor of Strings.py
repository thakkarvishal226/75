import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1[:math.gcd(len(str1),len(str2))] if str1+str2 == str2+str1 else ""





if __name__ == "__main__":
    str1 = "ABABAB"
    str2 = "AB"
    print(Solution().gcdOfStrings(str1,str2))