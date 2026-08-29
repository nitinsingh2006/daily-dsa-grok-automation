# Unique Pair Sum

**Difficulty:** Easy  
**Topic:** Arrays

Given an integer array and a target, count distinct unordered pairs whose sum equals target. Each element can be used at most once per pair. Return the count.

## Approach
Use a hash set to store seen numbers. For each number, check if target - number is in set and not yet counted. Use a second set to record pairs as tuples sorted to avoid duplicates.

## Complexity
O(n) time, O(n) space

## Solution
```python
def solve(nums,target):
    seen=set();pairs=set()
    for num in nums:
        comp=target-num
        if comp in seen:
            pairs.add(tuple(sorted((num,comp))))
        seen.add(num)
    return len(pairs)
```
