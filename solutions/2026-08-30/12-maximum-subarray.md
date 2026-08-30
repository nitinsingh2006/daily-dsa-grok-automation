# Maximum Subarray

**Difficulty:** Easy  
**Topic:** Dynamic Programming

Find the contiguous subarray with the largest sum in an integer array.

## Approach
Kadane's algorithm keeps current and global maximum.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):\n    cur=best=nums[0]\n    for n in nums[1:]:\n        cur=max(n, cur+n)\n        best=max(best, cur)\n    return best
```
