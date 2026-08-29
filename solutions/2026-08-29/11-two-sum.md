# Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

Find two indices in an array that sum to a target value. Return indices in any order. If no solution, return empty list.

## Approach
Use a hash map to store numbers and their indices while iterating.

## Complexity
O(n) time, O(n) space

## Solution
```python
def two_sum(nums,target):
    seen={}
    for i,num in enumerate(nums):
        comp=target-num
        if comp in seen:
            return [seen[comp],i]
        seen[num]=i
    return []
```
