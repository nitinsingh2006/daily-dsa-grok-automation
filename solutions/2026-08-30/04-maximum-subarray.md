# Maximum Subarray

**Difficulty:** Easy  
**Topic:** Dynamic Programming

Find the contiguous subarray with the largest sum.

## Approach
Kadane's algorithm maintains current and global maximums.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    max_ending=max_so_far=nums[0]
    for num in nums[1:]:
        max_ending=max(num,max_ending+num)
        max_so_far=max(max_so_far,max_ending)
    return max_so_far
```
