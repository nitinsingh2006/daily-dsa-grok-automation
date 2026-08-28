# Max Subarray Sum with One Deletion

**Difficulty:** Hard  
**Topic:** DP

Given an integer array nums, find the maximum sum of a non‑empty subarray after deleting at most one element.

## Approach
Maintain two DP states: keep (no deletion) and delete (one deletion used).

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray_sum_with_one_deletion(nums):
    n=len(nums)
    if n==0:return 0
    keep=nums[0]
    delete=0
    best=keep
    for i in range(1,n):
        delete=keep
        keep=max(nums[i],keep+nums[i])
        best=max(best,keep,delete)
    return best
```
