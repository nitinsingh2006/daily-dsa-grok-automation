# Maximum Subarray

**Difficulty:** Medium  
**Topic:** Arrays

Given an integer array, find the contiguous subarray with the largest sum.

## Approach
Kadane's algorithm keeps a running maximum and global maximum.

## Complexity
O(n) time, O(1) space

## Solution
```python
def solve(nums):
    max_ending=max_global=nums[0]
    for n in nums[1:]:
        max_ending=max(n,max_ending+n)
        max_global=max(max_global,max_ending)
    return max_global
```
