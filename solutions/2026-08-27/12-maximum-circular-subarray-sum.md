# Maximum Circular Subarray Sum

**Difficulty:** Hard  
**Topic:** Arrays

Given an array, find the maximum sum of a non‑empty subarray that may wrap around the end.

## Approach
Kadane for max and min subarray; max wrap = total - min subarray, compare with normal max.

## Complexity
O(n) time, O(1) space

## Solution
```python
def max_circular_subarray(nums):\n    n=len(nums)\n    max_end=nums[0]\n    max_sofar=nums[0]\n    min_end=nums[0]\n    min_sofar=nums[0]\n    total=nums[0]\n    for x in nums[1:]:\n        max_end=max(x, max_end+x)\n        max_sofar=max(max_sofar, max_end)\n        min_end=min(x, min_end+x)\n        min_sofar=min(min_sofar, min_end)\n        total+=x\n    max_wrap=total - min_sofar\n    if max_wrap==0:\n        return max_sofar\n    return max(max_sofar, max_wrap)
```
