class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n_interval = len(intervals)
        
        s = 0
        while s < n_interval:
            if intervals[s][1] >= newInterval[0]:
                break
            s += 1

        e = n_interval - 1
        while e >= 0:
            if intervals[e][0] <= newInterval[1]:
                break
            e -= 1
        
        print(s,e)
        result = []
        for i in range(s):
            result.append(intervals[i])
        
        start = min(intervals[s][0], newInterval[0]) if 0 <= s < n_interval else newInterval[0]
        end = max(intervals[e][1], newInterval[1]) if 0 <= e < n_interval else newInterval[1]
        result.append([start, end])
        
        for i in range(e+1,n_interval):
            result.append(intervals[i])

        return result
