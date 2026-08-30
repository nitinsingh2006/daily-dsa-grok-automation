# Subarray Sum Divisible by K

**Difficulty:** Medium  
**Topic:** Prefix Sum

Given an integer array nums and an integer k, count subarrays whose sum is divisible by k.

## Approach
Track prefix sums modulo k with a hashmap.

## Complexity
O(n) time, O(k) space

## Solution
```python
def subarraySumDivisibleByK(nums, k):
    from collections import defaultdict
    count = defaultdict(int)
    count[0] = 1
    prefix = 0
    ans = 0
    for num in nums:
        prefix = (prefix + num) % k
        ans += count[prefix]
        count[prefix] += 1
    return ans
```
