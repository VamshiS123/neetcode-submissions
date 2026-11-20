class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sletters = {}
        tletters = {}

        for character in s:
            if character in sletters:
                sletters[character] += 1
            else:
                sletters[character] = 1
    
        for character in t:
            if character in tletters:
                tletters[character] += 1
            else:
                tletters[character] = 1
        
        if sletters == tletters:
            return True
        else:
            return False