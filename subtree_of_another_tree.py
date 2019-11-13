def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.isthere(s,t)
        
        
def isthere(self, s, t):
    if s == None:
        return t == None

    # these above lines are nothing judt equals to below comment
    # if s is None and t is None return True
    # if s is not None and t is None return True
    # if s is None and t is not None return False 
    
    return self.issame(s, t) or self.isthere(s.left, t) or self.isthere(s.right, t)
    #  we are not using this
    #  if s.val == t.val:
    #      return issame(s,t)
    #  return issame(s.left,t) or issame(s.right,t)
    #   because what if s.val is equal to t.val but the issame function return false 
    #   then our ans will be false but we also need to check in the right and left of 
    #   the tree

    
def issame(self, s,t):
    if s == None:
        return t == None
    if t == None:
        return False    
    return s.val == t.val and self.issame(s.left, t.left) and self.issame(s.right, t.right)