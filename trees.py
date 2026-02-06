class Node:
    def __init__(self,val,Left=None,Right=None):
        self.val=val
        self.Left=Left
        self.Right=Right
def printer(k):
    if k==None:
        return
    printer(k.Left)
    print(k.val)
    printer(k.Right)

def size(p):
    if p==None:
        return 0
    return 1+size(p.Left)+size(p.Right)


a=Node(2,None,None)
b=Node(5,None,None)
c=Node(8,None,None)
d=Node(9,None,None)
e=Node(4,None,None)
f=Node(5)
g=Node(3)
 #       2
 #     5    8
 #   9  4  5  3
a.Left=b
a.Right=c
b.Left=d
b.Right=e
c.Left=f
c.Right=g
printer(a)
sized=size(a)
print("Size of Binary Tree:",sized)


