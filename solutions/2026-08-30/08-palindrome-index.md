# Palindrome Index

**Difficulty:** Medium  
**Topic:** Strings

Given a string, find the index of a character that can be removed to make the string a palindrome. If already palindrome, return -1. If impossible, return -2.

## Approach
Two-pointer check; if mismatch, try removing either side and test palindrome.

## Complexity
O(n) time, O(1) space

## Solution
```python
def palindrome_index(s):
    def is_pal(sub):
        return sub == sub[::-1]
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            if is_pal(s[l+1:r+1]):
                return l
            if is_pal(s[l:r]):
                return r
            return -2
        l += 1
        r -= 1
    return -1
```
