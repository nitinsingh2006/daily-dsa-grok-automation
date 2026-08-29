# Maximum Subarray

**Difficulty:** Medium  
**Topic:** Dynamic Programming

Return the largest sum of a contiguous subarray.

## Approach
Kadane's algorithm keeps current and global max.

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
