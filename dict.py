import math as m
d={'name':"Arpit Sahoo","date":"30/1/2016","Situation":"Learned git and has LL exam tommorow"}
print(d.__len__())
print(len(d))
print(d.__iter__())
_it=d.__iter__()
while True:
    try:
        x=next(_it)
        print(x)
    except StopIteration:
        break
