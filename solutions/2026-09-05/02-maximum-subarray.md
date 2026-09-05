# Maximum Subarray

**Difficulty:** Medium  
**Topic:** Arrays

Given an integer array nums, find the contiguous subarray with the largest sum and return its sum.

## Approach
Kadane's algorithm, keep current and best sums.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    best=curr=nums[0]
    for n in nums[1:]:
        curr=max(n,curr+n)
        best=max(best,curr)
    return best
```
