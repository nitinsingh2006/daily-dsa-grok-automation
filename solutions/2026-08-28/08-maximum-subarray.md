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
    max_ending = max_global = nums[0]
    for num in nums[1:]:
        max_ending = max(num, max_ending + num)
        max_global = max(max_global, max_ending)
    return max_global
```
