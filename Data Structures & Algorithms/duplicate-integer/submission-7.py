class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for number in nums:
            if number in hs:
                return True
            hs.add(number)
        return False

         