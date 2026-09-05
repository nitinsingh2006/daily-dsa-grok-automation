# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target.

## Approach
Use a hash map to store numbers and indices.

## Complexity
O(n) time, O(n) space

## Solution
```python
def two_sum(nums,target):
    d={}
    for i,n in enumerate(nums):
        if target-n in d:
            return [d[target-n],i]
        d[n]=i
    return []
```
