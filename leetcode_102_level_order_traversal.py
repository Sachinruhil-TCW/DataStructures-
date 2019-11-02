import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        res = []
        q = queue.Queue() #take a queue
        if root is None:
            return None
        
        q.put(root) #put the root in q
       
        while not q.empty(): 
            a = []
            size = q.qsize() #take the size of queue
            
            while size != 0:
                curr = q.get() #take out the root from queue
                a.append(curr.val)#append root in level wise array
                if curr.left is not None: # keep adding teh child nodes
                    q.put(curr.left)
                if curr.right is not None:
                    q.put(curr.right)
                size -= 1 
            if len(a) != 0:
                res.append(a)
        return res
                
        