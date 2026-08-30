# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Given an array of integers and a target sum, return the indices of the two numbers that add up to the target. Each input has exactly one solution, and you cannot use the same element twice.

## Approach
Use a hash map to store numbers and their indices while iterating.

## Complexity
O(n) time, O(n) space

## Solution
```python
def solve(nums,target):
    d={}
    for i,n in enumerate(nums):
        if target-n in d:
            return [d[target-n],i]
        d[n]=i
    return []
```
