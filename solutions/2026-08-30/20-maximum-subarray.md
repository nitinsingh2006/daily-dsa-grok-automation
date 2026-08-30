# Maximum Subarray

**Difficulty:** Medium  
**Topic:** Dynamic Programming

Given an integer array, find the contiguous subarray with the largest sum and return that sum.

## Approach
Use Kadane's algorithm to track current max ending here and global max.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):\n    max_ending = max_so_far = nums[0]\n    for num in nums[1:]:\n        max_ending = max(num, max_ending + num)\n        max_so_far = max(max_so_far, max_ending)\n    return max_so_far
```
