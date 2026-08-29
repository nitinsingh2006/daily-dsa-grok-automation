# Maximum Subarray

**Difficulty:** Easy  
**Topic:** Arrays

Return the maximum sum of any contiguous subarray.

## Approach
Kadane's algorithm keeps a running maximum.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):
    max_ending=max_so_far=nums[0]
    for x in nums[1:]:
        max_ending=max(x,max_ending+x)
        max_so_far=max(max_so_far,max_ending)
    return max_so_far
```
