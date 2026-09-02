class Solution:
    #U - 2 strings, they must be the same length, any word, count num of letr
    #M - Hashmap K = Character V = 
    #P - for every Char in S add to a map the char, if in the map, add 1 to V, do the same for T. 
    #I 
    #R
    #E
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if s and t are equal length! 
        if len(s) != len(t):
            return False
        # Make frequency dictionaries 
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)
        return dict_s == dict_t
