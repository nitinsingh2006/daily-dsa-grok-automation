# Reverse Subarray

**Difficulty:** Medium  
**Topic:** Arrays

Given an array and indices L and R, reverse the subarray from L to R in place.

## Approach
Use two pointers moving towards each other.

## Complexity
O(n) time, O(1) space

## Solution
```python
def reverse_subarray(arr,l,r):\n    while l<r:\n        arr[l],arr[r]=arr[r],arr[l]\n        l+=1\n        r-=1\n    return arr
```
