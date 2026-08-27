# Maximum Subarray

**Difficulty:** Easy  
**Topic:** Dynamic Programming

Find the contiguous subarray with the largest sum in a given integer array.

## Approach
Kadane's algorithm keeps current and global maximum while scanning.

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
