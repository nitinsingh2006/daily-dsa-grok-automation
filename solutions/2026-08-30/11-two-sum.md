# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Given an array of integers and a target, return indices of two numbers that add up to target.

## Approach
Use a hash map to store numbers and their indices.

## Complexity
O(n) time, O(n) space

## Solution
```python
def two_sum(nums, target):\n    d={}\n    for i,n in enumerate(nums):\n        if target-n in d:\n            return [d[target-n], i]\n        d[n]=i\n    return []
```
