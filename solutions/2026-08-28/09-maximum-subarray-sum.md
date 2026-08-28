# Maximum Subarray Sum

**Difficulty:** Medium  
**Topic:** Arrays

Given an integer array nums, return the largest sum of a contiguous subarray. The subarray must contain at least one element.

## Approach
Use Kadane's algorithm to keep track of current and maximum sums while iterating.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    max_ending = max_so_far = nums[0]
    for x in nums[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far
```
