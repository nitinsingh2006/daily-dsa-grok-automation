# Maximum Subarray

**Difficulty:** Easy  
**Topic:** Dynamic Programming

Find the contiguous subarray with the largest sum in an integer array.

## Approach
Kadane's algorithm keeps current and global max.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    best=curr=nums[0]
    for n in nums[1:]:
        curr=max(n, curr+n)
        best=max(best, curr)
    return best
```
