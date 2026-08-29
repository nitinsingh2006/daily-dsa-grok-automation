# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Find two indices of numbers that add up to a given target.

## Approach
Use a hash map to store seen numbers and their indices.

## Complexity
O(n) time, O(n) space

## Solution
```python
def two_sum(nums,target):
    d={}
    for i,x in enumerate(nums):
        if target-x in d:
            return [d[target-x],i]
        d[x]=i
    return []
```
