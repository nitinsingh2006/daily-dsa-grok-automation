# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Given an array of integers and a target, return indices of two numbers that add up to target.

## Approach
Use a hash map to store numbers and indices.

## Complexity
O(n) time, O(n) space

## Solution
```python
def two_sum(nums,target):
    d={}
    for i,num in enumerate(nums):
        if target-num in d:
            return [d[target-num],i]
        d[num]=i
    return []
```
