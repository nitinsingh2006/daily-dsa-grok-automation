# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Given an array of integers and a target, return indices of two numbers that add up to target.

## Approach
Use a hash map to store numbers and indices while iterating.

## Complexity
O(n) time, O(n) space

## Solution
```python
def solve(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i
    return []
```
