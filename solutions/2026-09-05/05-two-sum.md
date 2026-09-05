# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Given an array of integers and a target, return indices of two numbers that add up to target.

## Approach
Use a hash map to store complements.

## Complexity
O(n) time, O(n) space

## Solution
```python
def solve(nums,target):
    d={}
    for i,n in enumerate(nums):
        if n in d:
            return [d[n],i]
        d[target-n]=i
```
