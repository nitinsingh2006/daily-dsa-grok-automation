# Balanced Binary Tree

**Difficulty:** Hard  
**Topic:** Trees

Determine if a binary tree is height-balanced. A binary tree is balanced if the depths of the two subtrees of every node never differ by more than one.

## Approach
Post-order recursion to compute heights and balance status.

## Complexity
O(n) time, O(h) space

## Solution
```python
def isBalanced(root):
    def helper(node):
        if not node:
            return 0,True
        lh,lb=helper(node.left)
        rh,rb=helper(node.right)
        h=max(lh,rh)+1
        balanced=lb and rb and abs(lh-rh)<=1
        return h,balanced
    return helper(root)[1]}
```
