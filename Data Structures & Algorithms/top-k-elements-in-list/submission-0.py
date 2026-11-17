class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for i in range(0, len(nums) + 1)]

        for num, i in count.items():
            buckets[i].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        