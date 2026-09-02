class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Understand
        #Match
        #Plan
        #Impliment 
        #Run
        #Evaluate

    #Create a Set, Then add all nums into the set, Compare arr length vs set   length, and return False is they arent the same length
        my_set = set(nums)
        if len(my_set) != len(nums):
            return True
        else: 
            return False

        

