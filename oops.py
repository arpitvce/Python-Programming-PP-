class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def check(self):
        if self.age<18:
            print("ineligible to vote!")
        else :
            print("Eligible to vote!")
madhav=Student("Madhav",19)
madhav.check()
