class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for number in nums:
            if number in hashmap:
                return True
            else:
                hashmap[number] = True
        return False

         