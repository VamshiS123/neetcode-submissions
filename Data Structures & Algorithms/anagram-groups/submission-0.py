class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupofwords = {}

        for string in strs:

            arr = [0] * 26
            for letter in string:
                x = ord(letter) - ord('a')
                arr[x] += 1
            
            
            t = tuple(arr)

            if t not in groupofwords:
                groupofwords[t] = []
            
            groupofwords[t].append(string)

        return list(groupofwords.values())



            