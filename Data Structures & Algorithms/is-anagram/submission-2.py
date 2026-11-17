class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        map1 = {}
        map2 = {}

        for char in s:
            if char in map1:
                map1[char] += 1
            else:
                map1[char] = 1
            
        for char in t:
            if char in map2:
                map2[char] += 1
            else:
                map2[char] = 1

        if map1 == map2:
            return True
        else:
            return False

