# Maximum Subarray

**Difficulty:** Medium  
**Topic:** Dynamic Programming

Given an integer array, find the contiguous subarray with the largest sum and return that sum. Use Kadane's algorithm for linear time.

## Approach
Iterate once, keeping current and global maximum sums.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    max_ending=max_global=nums[0]
    for n in nums[1:]:
        max_ending=max(n,max_ending+n)
        max_global=max(max_global,max_ending)
    return max_global
```
