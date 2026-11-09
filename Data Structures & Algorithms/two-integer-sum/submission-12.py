class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for idx,val in enumerate(nums):
            compliment = target - val
            if compliment in compliments:
                return [compliments[compliment], idx]
            else:
                compliments[val] = idx
