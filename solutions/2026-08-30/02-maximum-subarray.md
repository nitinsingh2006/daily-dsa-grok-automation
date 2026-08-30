# Maximum Subarray

**Difficulty:** Easy  
**Topic:** Arrays

Return the largest sum of a contiguous subarray.

## Approach
Kadane's algorithm tracks current and max sums while iterating.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums): max_sum=curr=nums[0];
    for n in nums[1:]:
        curr=max(n,curr+n)
        max_sum=max(max_sum,curr)
    return max_sum
```
