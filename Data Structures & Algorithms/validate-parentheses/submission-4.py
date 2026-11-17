class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')' : '(', '}' : '{' , ']' : '[' }
        stack = []

        for char in s:
            if char in pair:
                if len(stack) == 0 or stack[-1] != pair[char]:
                    return False
                stack.pop()
            
            else:
                stack.append(char)

        return not stack