# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Find two indices in an array that sum to target.

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
    return []
```
