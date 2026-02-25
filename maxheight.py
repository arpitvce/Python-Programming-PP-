# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def findlefth(root):
            if root is None:
                return 0
            else:
                return 1+max(findlefth(root.left),findlefth(root.right))
        def findrighth(root):
            if root is None:
                return 0
            else:
                return 1+max(findrighth(root.right),findrighth(root.left))   
        def findmax(root,maxi):
            if root==None:
                return
            lh=findlefth(root.left)
            rh=findrighth(root.right)
            maxi[0]=max(maxi[0],lh+rh)
            findmax(root.left,maxi)
            findmax(root.right,maxi)
        maxh=[0]
        findmax(root,maxh)
        return maxh[0]
