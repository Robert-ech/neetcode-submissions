class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Build default dict for keys that dont yet exist
        res = defaultdict(list)
        # For loop through every word in the list
        for s in strs:
            count = [0] * 26 # <- create 26 possible letters in a list
        # For every letter in the word!
        # Use the ASCII value of the char, subtract ASCII(a) to get its index
        # add 1 to the count[index]
            for c in s:
                count[ord(c) - ord('a')] += 1 #<- Add 1 to that index for that char
        # Add the word signature we built to add it to our defaultdict
        # If the key is recognized, the word s gets added as a value
        # If it doesn't recognize the key, it gets added to the dict
            res[tuple(count)].append(s)
        # Return the Hashmaps values as a list!
        return list(res.values())