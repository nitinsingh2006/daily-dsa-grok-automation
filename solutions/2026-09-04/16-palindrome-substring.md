# Palindrome Substring

**Difficulty:** Medium  
**Topic:** Strings

Count all palindromic substrings in a string.

## Approach
Expand around centers for each character pair.

## Complexity
O(n^2) time, O(1) space

## Solution
```python
def solve(s):
    n=len(s)
    count=0
    for center in range(2*n-1):
        l=center//2
        r=l+center%2
        while l>=0 and r<n and s[l]==s[r]:
            count+=1
            l-=1
            r+=1
    return count
```
