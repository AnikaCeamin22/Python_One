#Day6
#chapter8 (OOPs2)
#del
"""
used to delete object properties or object itself
del obj_name.attribute
del object_name
"""
#private(like not real) attributes and methods
"""
are meant to be used only wityhin the class and are not accessible from outside the class.
Conceptual Implementations in python
privat : __method_name(self):
          __self.password=password # attribute
"""
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no= acc_no
        self.__acc_pass=acc_pass

    def __reset_pass(self):
        print(self.__acc_pass)

    def get_password(self):
        self.__reset_pass()

a=Account(200,1234)
#a.reset_pass() not work
#a.__acc_pass not work
a.get_password()

#Inheritance
"""
Types:
1.single
2.Multi-level
3.Mutiple
"""
#Exa:
class Father:
    gen="Male"
    def __init__(self,type):
        self.type=type

    @staticmethod
    def F():
        print("get from Father")

    def gender1(self):
        print(self.type)
        if(self.type==1):
            print("YES,",self.gen)
            self.F()
        else: print("NO,")
        self.F()
class Mother:
    gen="Female"
    @staticmethod
    def M():
        print("get from Mother")
    def gender2(self):
        if("Female"==self.gen):
            print("YES,")
            self.M()
        else: print("NO,")
        self.M()
class Son(Father):
    def __init__(self,type):
        super().__init__(type)

class Dauther(Father,Mother):
    def __init__(self,x):
        self.gen=x
B=Son(2)
print(B.type)
print(B.gen)
B.gender1()
#super: is used to access methods of the parent class.
"""
super.__init__(self,attributes)
super().Parent_method_name
"""
#@classmethod -> decorator
"""
is bound to the class and receivews the class as an implicit first argument.
static method can't access or modify class state and generally for utility.
@classmethod
def change(cls)
pass
"""
# self -> object
#Exa:
class Person:
    name="ANIKA"
    def change(obj,name):
        obj.name=name
    @classmethod
    def Change(cls,name):
        cls.name=name
p=Person()
p.change("Hello")
print(p.name)
print(Person.name)
p1=Person()
p1.Change("World")
print(p1.name)
print(Person.name)

""""
1.instance methods(object)
2.static methods
3.class methods(class)
"""
#property:we use this decorator on any method in tne class to use the method as a property.
"""
it convert a function into a changable attribute
"""
class Std:
    abc=0
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.abc=self.a+self.b+self.c/3
    def Avg(self):
        self.abc=self.a+self.b+self.c/3
    @property
    def avg(self):
        return(self.a+self.b+self.c)/3
s=Std(10,20,30)
print(s.abc)
print(s.avg)
s.a=30
print(s.abc)
print(s.avg)
#Polymorphism
"""
sreaching : Emulating numeric type
"""
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def Num(self):
        print(self.real," + ",self.img,"j")
    def __add__(self,num):
        x=self.real+num.real
        y=self.img+num.img
        return Complex(x,y)
n1=Complex(2,3)
n2=Complex(4,5)
n=n1+n2
n.Num()





    




    

    







