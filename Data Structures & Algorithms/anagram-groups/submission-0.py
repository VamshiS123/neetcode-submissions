class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through the whole strs
        # loop through each of the strings
        # count each of the things in an array
        # make it into a tuple
        # put all of it into a hashmap and use the tuple as the key
        final = {}
        for string in strs:

            array = [0]*26
            
            for char in string:
                idx = ord(char) - ord('a')
                array[idx] += 1
            
            t = tuple(array)

            if t not in final:
                final[t] = []
            
            final[t].append(string)
        
        return list(final.values())