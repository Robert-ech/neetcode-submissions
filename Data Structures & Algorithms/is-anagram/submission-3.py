class Solution:
    #U - 2 strings, they must be the same length, any word, count num of letr
    #M - Hashmap K = Character V = 
    #P - for every Char in S add to a map the char, if in the map, add 1 to V, do the same for T. 
    #I 
    #R
    #E
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_s = {}
        my_t = {}

        for i in range(len(s)):
            my_s[s[i]] = 1 + my_s.get(s[i], 0)
            my_t[t[i]] = 1 + my_t.get(t[i], 0)

        return my_s == my_t
        