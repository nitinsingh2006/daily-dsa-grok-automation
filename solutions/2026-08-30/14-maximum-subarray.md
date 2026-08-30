# Maximum Subarray

**Difficulty:** Medium  
**Topic:** Dynamic Programming

Find the contiguous subarray with the largest sum in an integer array.

## Approach
Kadane's algorithm tracks current and global maximum.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    best=cur=nums[0]
    for n in nums[1:]:
        cur=max(n,cur+n)
        best=max(best,cur)
    return best
```
