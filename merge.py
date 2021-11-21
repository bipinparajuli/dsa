# intervals = [[1,3],[2,6],[8,10],[15,18]]

def merge(intervals):
        Start = 0
        End = 1
        
        if not intervals:
            return []
        
        intervals.sort()
        print(intervals)
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            prev = merged[-1]
            print(prev)
            overlap_with_prev = curr[Start] <= prev[End]
            
            if overlap_with_prev:
                can_extend = curr[End] > prev[End]
                if can_extend:
                    merged[-1] = [prev[Start], curr[End]]
            else:
                merged.append(curr)
                
        return merged

print(merge([[2,6],[1,3],[8,10],[15,18]]))