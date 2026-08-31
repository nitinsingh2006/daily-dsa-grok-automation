# Minimum Swaps to Sort Array

**Difficulty:** Hard  
**Topic:** Arrays

Given an array of distinct integers, find the minimum number of swaps needed to sort it in ascending order.

## Approach
Use cycle detection after sorting positions; each cycle of size k requires k-1 swaps.

## Complexity
O(n log n) time, O(n) space

## Solution
```python
def min_swaps(arr):\n    n=len(arr)\n    arrpos=sorted(enumerate(arr), key=lambda it: it[1])\n    visited=[False]*n\n    swaps=0\n    for i in range(n):\n        if visited[i] or arrpos[i][0]==i:\n            continue\n        cycle_size=0\n        j=i\n        while not visited[j]:\n            visited[j]=True\n            j=arrpos[j][0]\n            cycle_size+=1\n        if cycle_size>0:\n            swaps+=cycle_size-1\n    return swaps
```
