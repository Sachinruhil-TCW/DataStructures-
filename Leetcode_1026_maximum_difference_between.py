sumof = float("-inf")
def maxAncestorDiff(self, root: TreeNode) -> int:
    if root is None:
        return None
    min_val = float("inf")
    max_val = float("-inf")
    
    
    self.helper(root, min_val, max_val)
    return self.sumof

    
def helper(self, root, min_val, max_val):
    
    if root is None:
        # print(max_val-min_val)
        if max_val - min_val > self.sumof:
            self.sumof = max_val - min_val
        return  
    if min_val > root.val:
        min_val = root.val
    if max_val < root.val:
        max_val = root.val
    # print(min_val)
    self.helper(root.left, min_val, max_val)
    self.helper(root.right, min_val, max_val)
    
    