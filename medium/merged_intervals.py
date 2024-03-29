def mergeOverlappingIntervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0]) # sort by first index value of each list element
    merged_interval = []
    current_interval = sorted_intervals[0]
    merged_interval.append(current_interval)

    for next_interval in sorted_intervals:
        _, current_interval_end = current_interval
        next_interval_start, next_interval_end  = next_interval

        if current_interval_end >= next_interval_start:
            current_interval[1] = max(current_interval_end, next_interval_end)
        else:
            current_interval = next_interval
            merged_interval.append(current_interval)
    
    return merged_interval