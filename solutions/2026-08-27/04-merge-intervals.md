# Merge Intervals

**Difficulty:** Medium  
**Topic:** Intervals

Merge all overlapping intervals in a list of intervals and return the non-overlapping intervals sorted by start time.

## Approach
Sort by start, then merge sequentially.

## Complexity
O(n log n) time, O(n) space

## Solution
```python
def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x:x[0])
    merged=[intervals[0]]
    for curr in intervals[1:]:
        last=merged[-1]
        if curr[0]<=last[1]:
            last[1]=max(last[1],curr[1])
        else:
            merged.append(curr)
    return merged
```
