class Solution:
    def isValid(self, s: str) -> bool:
        # go through s
        # check if its a opening
        # if its an opening add to stack
        # if its in brackets compare to stack
        brackets = {')':'(', '}':'{', ']':'['}

        stack = []

        for char in s:
            if char in brackets and stack:
                if stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)
        return not stack