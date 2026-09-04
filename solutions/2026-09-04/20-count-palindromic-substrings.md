# Count Palindromic Substrings

**Difficulty:** Hard  
**Topic:** Strings

Given a string, count all substrings that are palindromes.

## Approach
Expand around each center to count palindromes.

## Complexity
O(n^2) time, O(1) space

## Solution
```python
def count_palindromes(s):
    n=len(s)
    count=0
    for center in range(n):
        l=r=center
        while l>=0 and r<n and s[l]==s[r]:
            count+=1
            l-=1
            r+=1
        l=center
        r=center+1
        while l>=0 and r<n and s[l]==s[r]:
            count+=1
            l-=1
            r+=1
    return count
```
