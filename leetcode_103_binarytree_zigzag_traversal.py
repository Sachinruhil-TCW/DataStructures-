class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret = []
        self._zigzagLevelOrder(root, 0, ret)
        return ret

    def _zigzagLevelOrder(self, root, level, ret):
        if len(ret) < level + 1:
            ret.append([])

        left = root.left
        right = root.right

        if level % 2 == 1:
            ret[level].append(root.val)
        else:
            ret[level].insert(0,root.val)
            
        if right:
            self._zigzagLevelOrder(right, level + 1, ret)
        if left:
            self._zigzagLevelOrder(left, level + 1, ret)
