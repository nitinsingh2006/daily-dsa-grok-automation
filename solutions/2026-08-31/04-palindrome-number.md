# Palindrome Number

**Difficulty:** Easy  
**Topic:** Math

Determine if an integer is a palindrome without converting to string.

## Approach
Reverse half of the number and compare with the other half.

## Complexity
O(log10(n)) time, O(1) space

## Solution
```python
def solve(x):
    if x<0 or (x%10==0 and x!=0):
        return False
    rev=0
    while x>rev:
        rev=rev*10+x%10
        x//=10
    return x==rev or x==rev//10
```
