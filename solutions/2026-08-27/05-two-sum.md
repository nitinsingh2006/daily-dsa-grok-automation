# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Find two indices in an array that sum to a target value.

## Approach
Use a hash map to store seen numbers and their indices.

## Complexity
O(n) time, O(n) space

## Solution
```python
def solve(nums,target):
    seen={}
    for i,n in enumerate(nums):
        if target-n in seen:
            return [seen[target-n],i]
        seen[n]=i
    return []
```
