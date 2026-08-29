# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Find two indices in an array that sum to a target.

## Approach
Use a hash map to store numbers and indices.

## Complexity
O(n) time, O(n) space

## Solution
```python
def solve(nums,target):\n    d={}\n    for i,n in enumerate(nums):\n        if target-n in d:\n            return [d[target-n],i]\n        d[n]=i\n    return []
```
