#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #find node of root that matches subroot
        if subRoot is None:
            return True
        if root is None:
            return False
        
        
        # We need to find a starting point in the big tree
        if self.sameTree(root, subRoot):
            return True
        #If not starting point is found then we nee to traverse left or right of the big tree
        return self.isSubtree(root.right, subRoot) or  self.isSubtree(root.left, subRoot) 
    def sameTree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.val != subRoot.val:
            return False

        return self.sameTree(root.right, subRoot.right) and self.sameTree(root.left, subRoot.left)