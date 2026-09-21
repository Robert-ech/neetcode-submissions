class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for char in s.strip():
            if char in letters:
                letters[char] = 1 + letters.get(char, 0)
            else:
                letters[char] = 1
        for char in t.strip():
            if char not in letters:
                return False
            letters[char] -= 1
            if letters[char] == 0:
                del letters[char]
        return not letters