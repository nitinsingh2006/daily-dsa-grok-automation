# Balanced Parentheses

**Difficulty:** Easy  
**Topic:** Strings

Check if a string of parentheses is balanced.

## Approach
Use a stack.

## Complexity
O(n) time, O(n) space

## Solution
```python
def is_balanced(s):\n    stack=[]\n    mapping={')':'(', '}':'{', ']':'['}\n    for c in s:\n        if c in mapping.values():\n            stack.append(c)\n        elif c in mapping:\n            if not stack or stack[-1]!=mapping[c]:\n                return False\n            stack.pop()\n    return not stack
```
