# Maximum Subarray

**Difficulty:** Easy  
**Topic:** Dynamic Programming

Given an integer array, find the contiguous subarray with the largest sum and return that sum.

## Approach
Kadane's algorithm: iterate, keep current max ending here, update global max.

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
