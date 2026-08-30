# Maximum Subarray

**Difficulty:** Medium  
**Topic:** Dynamic Programming

Given an integer array, find the contiguous subarray with the largest sum and return that sum.

## Approach
Use Kadane's algorithm to keep track of the maximum ending here and the global maximum.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    max_ending=curr=nums[0]
    for n in nums[1:]:
        curr=max(n,curr+n)
        max_ending=max(max_ending,curr)
    return max_ending
```
