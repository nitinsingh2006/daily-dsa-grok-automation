# Maximum Subarray Sum

**Difficulty:** Medium  
**Topic:** Arrays

Given an integer array, find the contiguous subarray with the maximum sum.

## Approach
Kadane's algorithm maintains current and global maximum.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):\n    max_ending=0\n    max_so_far=nums[0]\n    for x in nums:\n        max_ending=max(x,max_ending+x)\n        max_so_far=max(max_so_far,max_ending)\n    return max_so_far
```
