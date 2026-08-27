# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Given an array of integers and a target sum, return indices of two numbers that add up to the target. Each input has exactly one solution, and you cannot reuse an element.

## Approach
Use a hash map to store seen numbers and their indices.

## Complexity
O(n) time, O(n) space

## Solution
```python
def solve(nums,target):
    lookup={}
    for i,num in enumerate(nums):
        if target-num in lookup:
            return [lookup[target-num],i]
        lookup[num]=i
    return []
```
