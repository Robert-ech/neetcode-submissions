class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        originals = set()
        for num in nums:
            originals.add(num)
        if len(originals) != len(nums):
            return True
        else:
            return False