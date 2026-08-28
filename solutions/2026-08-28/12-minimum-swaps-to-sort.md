# Minimum Swaps to Sort

**Difficulty:** Medium  
**Topic:** Graphs

Given an array of distinct integers from 1 to n, determine the minimum number of swaps required to sort the array in ascending order.

## Approach
Treat the array as a graph of cycles; each cycle of length k needs k-1 swaps.

## Complexity
O(n) time, O(n) space

## Solution
```python
def min_swaps(arr):
    n = len(arr)
    visited = [False]*n
    swaps = 0
    for i in range(n):
        if visited[i] or arr[i]==i+1:
            continue
        cycle_len = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr[j]-1
            cycle_len += 1
        if cycle_len>0:
            swaps += cycle_len-1
    return swaps
```
