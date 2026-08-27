# Maximum Subarray Sum

**Difficulty:** Easy  
**Topic:** Arrays

Find the maximum sum of any contiguous subarray in a list of integers.

## Approach
Apply Kadane's algorithm to track current and best sums.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_subarray(nums):\n    max_ending=0\n    max_so_far=float('-inf')\n    for x in nums:\n        max_ending=max(x,max_ending+x)\n        max_so_far=max(max_so_far,max_ending)\n    return max_so_far
```
