class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in ('{', '[', '('):
                stack.append(c)
            elif not stack or stack.pop() != parenthesis[c]:
                return False
        return (not stack)