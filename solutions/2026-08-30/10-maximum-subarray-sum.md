# Maximum Subarray Sum

**Difficulty:** Medium  
**Topic:** Dynamic Programming

Given an integer array, find the contiguous subarray with the largest sum and return that sum. The array contains at least one number.

## Approach
Kadane's algorithm: iterate, keep current max and global max.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    cur=best=nums[0]
    for n in nums[1:]:
        cur=max(n,cur+n)
        best=max(best,cur)
    return best
```
