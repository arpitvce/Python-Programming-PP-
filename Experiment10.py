# Question 1
#import math
#a=int(input("enter a:"))
#c=math.factorial(a)
#print("factorial of",a,"=",c)

#Question 2
#import math
#a=int(input("enter angle:(in degrees)"))
#angle=math.radians(a)
#print("sine(a)=",math.sin(angle))
#print("cosine(a)=",math.cos(angle))
#print("tan(a)=",math.tan(angle))

#Question 3&4
#import calendar
#y=int(input("Enter year:"))
#m=int(input("Enter month:"))
#c=calendar.month(y,m)
#print("C is a leap year",calendar.isleap(y))
#print(c)

#Question 5
#import calendar
#m=int(input("Enter month:"))
#calendar.prmonth(2019,m)

#question 6
#import turtle
#for i in range(4):
#    turtle.forward(100)
#    turtle.left(90)
#turtle.circle(100)
#turtle.color("Red")

#question 7
#import turtle
#def circle(radius):
#    turtle.circle(radius)
#    for i in range (radius,radius+20,4):
#        turtle.circle(i)
#    turtle.done()
#circle(90)

#Question 8:
import turtle
for i in range(0,6):
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.right(120)


