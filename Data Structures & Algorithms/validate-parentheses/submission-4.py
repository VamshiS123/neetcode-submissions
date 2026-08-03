class Solution:
    def isValid(self, s: str) -> bool:
        map = {}
        map[")"] = "("
        map["}"] = "{"
        map["]"] = "["

        stack = []

        for bracket in s:
            if bracket in map: 
                if not stack or stack[-1] != map[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        
        if not stack:
            return True
        else:
            return False

            
