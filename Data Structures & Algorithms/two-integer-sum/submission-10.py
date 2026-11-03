class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, val in enumerate(nums):
            compliment = target - val
            if seen and compliment in seen:
                return [seen[compliment], idx]
            else:
                seen[val] = idx
        return -1