class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create seen dict
        seen = {}
        #traverse via k,v
        for i,num in enumerate(nums):
            #define compliment
            compliment = target - num
            if compliment in seen:
                return [seen[compliment], i]
            seen[num] = i