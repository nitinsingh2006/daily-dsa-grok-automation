# Maximum Subarray Sum

**Difficulty:** Medium  
**Topic:** Arrays

Given an integer array, find the contiguous subarray with the largest sum.

## Approach
Iterate, keep current sum and max.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):\n    max_sum=cur=nums[0]\n    for n in nums[1:]:\n        cur=max(n,cur+n)\n        max_sum=max(max_sum,cur)\n    return max_sum
```
