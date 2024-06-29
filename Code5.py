#Day5
#chapter8 (OOpS)
"""
To map with real world scenarios,we started using objects in code.
Procedural -> functional -> Objcet Oriented Programming

class: is a blueprint for creating objects.
#creating class
class Class_name:
   attibutes
   functions
#creating object(instance)
obj_name=class_name()
print(c.attibutes)
"""
class Student:
    name="Anika"
    age="23"
    roll="BFH2001026F"

s1=Student()
print(s1)
print(s1.name)
#__int__ function or Constructor
"""
all classes have a function called __int__(), which is always executed when the class is being initiated.

The 'self' parameter is a reference to the current instance of the class and
 is used to access variables that belongs to the class.
"""
class Student:
    university="NSTU" # class attributes
    #default constructor
    def __init__(self):
        print(self)
        print("Adding new student in Database....")
        pass
    #parameterized constructor
    def __init__(self,name):
        self.name=name # object attributes
        print("END")
    def hello(self):
        print("Methods starting," + self.name)

s2=Student("Richa")
print(s2.name)
s2.name="CEamin" #can change 
print(s2.name)
print(s2.university)
print(Student.university)
#s3=Student()
#object attributes prority is higher than class attributes

#Methods: are functions that belong to objects
s2.hello()
#Static Methods
"""
methods that don't use the self parameter(work at class level)
when wew don;t need to use any thing from object then it cna use
@staticmethod #decorator
def college():
  print(....)
"""
#Decorators:
"""
is a function which takes function as parameter and gives another function
allow us to wrap anooother function in order to extend the behaviour of the wrapped function,without permanently modyifying it.
"""
class Car:
    type="ABC"
    def __init__(self,cost):
       self.cost=cost
    @staticmethod
    def Show():
        print("Welcom to Car Shope")
    """@staticmethod
    def Cost():
        print(cost) # not work """
c1=Car(200)
c1.Show()
#Pilar of OOPs
""""
1.Abstraction: hiding the implementation details of a class and only showing the essential features to the user.
2.Encapsulation: wrapping data and functions into a single unit(object).
3.Inheritance:when one class(derived/child) derives the properties and methods of another class(base/parent)
4.Polymonphism:when the same operator is allowed to have different meaning according to the context.
"""
class Car:
    def __init__(self):
        self.bk=False
        self.acc=False
        self.clu=False
    def start(self):
        self.acc=False
        self.clu=False
        print("Car Starting......")
c=Car()
c.start()
#Exa:
class Account:
    def __init__(self,b,b_no):
        self.b=b
        self.b_no=b_no
    def debit(self,x):
        self.b-=x
        print("total balance: ",self.get_B())
    def credit(self,x):
        self.b+=x
        print("total balance: ",self.get_B())
    def get_B(self):
        return self.b
ac=Account(100,200)
ac.debit(50)
ac.credit(100)





        
    







