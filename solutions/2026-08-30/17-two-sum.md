# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Find two indices in an array such that the numbers at those indices add up to a given target. Return the indices as a list. If no such pair exists, return an empty list.

## Approach
Use a hash map.

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
