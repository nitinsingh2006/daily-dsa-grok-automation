# Maximum Subarray

**Difficulty:** Medium  
**Topic:** Arrays

Given an integer array, find the contiguous subarray with the largest sum and return that sum. Use Kadane's algorithm for linear time solution.

## Approach
Apply Kadane's algorithm, maintaining current max ending here and global max.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    max_ending = max_so_far = nums[0]
    for num in nums[1:]:
        max_ending = max(num, max_ending + num)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far
```
