# First Missing Positive

**Difficulty:** Medium  
**Topic:** Arrays

Given an unsorted array, return the smallest positive integer not present.

## Approach
Place each number at its correct index using swaps.

## Complexity
O(n) time, O(1) space

## Solution
```python
def first_missing(nums):\n    n=len(nums)\n    for i in range(n):\n        while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:\n            nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]\n    for i in range(n):\n        if nums[i]!=i+1:\n            return i+1\n    return n+1
```
