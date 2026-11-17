class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        best = 0
        left = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])

            best = max(best, right - left + 1)
        
        return best
            

            # two cases
            # first case if its not in seen, add the to seen
            # and advance the pointer and cal the best

            # secodn case is if its in seen, then advace the left pointer 

            