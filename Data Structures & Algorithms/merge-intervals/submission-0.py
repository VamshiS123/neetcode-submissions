class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort the list
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        # itreate to the list keep key and value
        for start, end in intervals[1: ]:

            last = merged[-1]

            if last[1] >= start:
                last[1] = max(last[1], end)
            else:
                merged.append([start, end])
        
        return merged

