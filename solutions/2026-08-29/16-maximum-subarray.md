# Maximum Subarray

**Difficulty:** Easy  
**Topic:** Arrays

Find the contiguous subarray with the largest sum in an integer array.

## Approach
Kadane's algorithm: track current and maximum sums.

## Complexity
O(n) time, O(1) space

## Solution
```python
def solve(nums):\n    max_so_far=curr=nums[0]\n    for n in nums[1:]:\n        curr=max(n,curr+n)\n        max_so_far=max(max_so_far,curr)\n    return max_so_far
```
