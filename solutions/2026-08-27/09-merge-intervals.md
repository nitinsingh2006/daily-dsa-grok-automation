# Merge Intervals

**Difficulty:** Medium  
**Topic:** Intervals

Merge overlapping intervals in a list of intervals.

## Approach
Sort intervals by start, then merge while iterating.

## Complexity
O(n log n) time, O(n) space

## Solution
```python
def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged
```
