# Maximum Subarray

**Difficulty:** Easy  
**Topic:** Arrays

Return the largest sum of a contiguous subarray.

## Approach
Kadane's algorithm tracks current and max sums.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    max_ending=max_so_far=nums[0]
    for n in nums[1:]:
        max_ending=max(n,max_ending+n)
        max_so_far=max(max_so_far,max_ending)
    return max_so_far
```
