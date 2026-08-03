class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        duplicate = set()

        for n in nums:

            if n in duplicate:
                flag = True

            duplicate.add(n)
        
        return flag

