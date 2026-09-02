class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = []
        for c in s:
            if c.isalnum():
               n.append(c)
        s = "".join(n).lower()
        print(s)
        print(s[::-1])
        return s == s[::-1]