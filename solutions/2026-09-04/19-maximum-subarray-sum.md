# Maximum Subarray Sum

**Difficulty:** Medium  
**Topic:** Arrays

Given an integer array, find the contiguous subarray with the largest sum.

## Approach
Use Kadane's algorithm to track current and maximum sums.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    max_ending=max_so_far=nums[0]
    for x in nums[1:]:
        max_ending=x if max_ending<0 else max_ending+x
        max_so_far=max(max_so_far,max_ending)
    return max_so_far
```
