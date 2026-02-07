from collections import deque
class Node:
    def __init__ (self,value,left=None,right=None):
        self.val=value
        self.left=left
        self.right=right
    def breadth(self):
        q=deque()
        q.append(self)
        while len(q)>0:
            temp=q.popleft()
            print(temp.val)
            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)

#        9
#      7  -1
#     8 7 5 0
a=Node(3)
b=Node(4)
c=Node(2)
d=Node(-1)
e=Node(1)
f=Node(7)
g=Node(9)
h=Node(6)
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g
e.left=h
a.breadth()






