'''Merge overlapping intervals.

Sort by interval start, then extend the previous range when the next one overlaps or touches. 
'''
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals = sorted(intervals, key=lambda item: item[0])

    merged_intervals = []

    for interval in intervals:
        if len(merged_intervals) == 0:
            merged_intervals.append([*interval])
            continue
        

        last_interval = merged_intervals[-1]

        # if start of current interval in last interval, extend. otherwise append new
        if interval[0] <= last_interval[1]:
            last_interval[1] = max(interval[1], last_interval[1])
        else:
            merged_intervals.append([*interval])
        
    return merged_intervals