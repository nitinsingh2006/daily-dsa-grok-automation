# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Given an integer array nums and an integer target, return indices of two numbers such that they add up to target. Each input has exactly one solution, and you may not reuse the same element twice.

## Approach
Use a hash map to store numbers and their indices while iterating.

## Complexity
O(n) time, O(n) space

## Solution
```python
def solve(nums, target):\n    d={}\n    for i,n in enumerate(nums):\n        if target-n in d:\n            return [d[target-n], i]\n        d[n]=i\n    return []
```
