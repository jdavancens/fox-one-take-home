def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge overlapping intervals.

    Sort intevals, then extend an interval when the next one overlaps or touches.
    Copy intervals so we don't mutate the caller's list.
    """

    # sort by interval start
    intervals = sorted(intervals, key=lambda item: item[0])

    merged_intervals = []

    for interval in intervals:

        # just add the first interval
        if len(merged_intervals) == 0:
            merged_intervals.append([*interval])
            continue

        last_interval = merged_intervals[-1]

        if interval[0] <= last_interval[1]:
            last_interval[1] = max(interval[1], last_interval[1])
        else:
            merged_intervals.append([*interval])
        
    return merged_intervals