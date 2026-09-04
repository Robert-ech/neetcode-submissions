class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # build word
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

        # Use default dict for entry creation 
        # For every word
        # Create an empty list of lists with 0s initialized for every letter
        # This creates a signature
        # for letter in word, use ascii values to add 1 to the value
        # of the index of the letter
        # Use the signature as a key to store the word in the correct
        # Bucket, then return the dict.value() as a list
                


