class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        map = {}
        map1 = {}

        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 0
        
        for char in t:
            if char in map1:
                map1[char] += 1
            else:
                map1[char] = 0

        if map == map1:
            return True
        else:
            return False