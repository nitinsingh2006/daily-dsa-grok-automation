# Unique Triplet Sum Zero

**Difficulty:** Medium  
**Topic:** Arrays

Given an integer array, count distinct triplets (i<j<k) whose sum is zero. Return the count.

## Approach
Sort and use two‑pointer to find pairs for each fixed element, skipping duplicates.

## Complexity
O(n^2) time, O(1) space

## Solution
```python
def count_zero_triplets(nums):\n    nums.sort()\n    n=len(nums)\n    count=0\n    for i in range(n-2):\n        if i>0 and nums[i]==nums[i-1]:\n            continue\n        left=i+1\n        right=n-1\n        while left<right:\n            s=nums[i]+nums[left]+nums[right]\n            if s==0:\n                count+=1\n                left+=1\n                right-=1\n                while left<right and nums[left]==nums[left-1]:\n                    left+=1\n                while left<right and nums[right]==nums[right+1]:\n                    right-=1\n            elif s<0:\n                left+=1\n            else:\n                right-=1\n    return count
```
