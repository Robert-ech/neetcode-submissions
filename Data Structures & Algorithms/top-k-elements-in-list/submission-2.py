class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build Freq Map
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        # create freq hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0) 
        # map the freq to index and number to value     
        for key,value in count.items():
            freq[value].append(key)

        res = []
        # traverse from the end to the begining
        for i in range(len(freq) -1, 0, -1):
            # do if num exists in freq[i]
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            