# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Given an array of integers and a target sum, return indices of two numbers that add up to target.

## Approach
Use hash map to store complement.

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
