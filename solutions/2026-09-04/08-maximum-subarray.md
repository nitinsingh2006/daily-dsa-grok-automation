# Maximum Subarray

**Difficulty:** Medium  
**Topic:** Dynamic Programming

Given an integer array, find the contiguous subarray with the largest sum and return that sum.

## Approach
Use Kadane's algorithm to track current and maximum sums while iterating.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):\n    max_ending=curr=nums[0]\n    for n in nums[1:]:\n        curr=max(n,curr+n)\n        max_ending=max(max_ending,curr)\n    return max_ending
```
