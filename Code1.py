#Day one
#chapter1
#output
print("Hello World")
print ( "Anika Ceamin","Richa" )

#variables
a=26
b=23.00
s="DoTheWork" #s='DO' or s='''Do'''
print(s,a)
print(a+b)
print(type(s))
print(type(a+b))
#Data Type: 1.integer,2.float,3.string,4.boolean,5.none
d=None
print(type(d))
#case secetype
#Types of Tokens
#1.punctuators:are symbole to orgranize sentence structure in proramming
#Exa: (),{},@,[],#,-=,+=,*=,/=,=...
#implicit type language(not need to tell variables type)
#Expression Execution:
print(2*s*3)
c="AS"
print(s+c) # concatenation
e=a//b
print(a/b,  e) #float
print(a//b) # int -> fool gives
#mod
print(5%-2)
print(-5%2)
print(-5%-2)
"""Three time 
Quotations for multi line comments"""
#input:
x=input("x :")
y=int(input("y:"))
z=float(input("b:"))
print(x, y,z)
#conditional statementd:
#if-elif-else (conditon):
#python is an indentation(proper spaceing) language
if(x=="Red") : 
    print("Stop")
elif(x=='Green') :
    print("GO")
elif(x=="Yellow") :
    print("Look")
else :
    print("anything")
#Single Line if/Ternary Operator
#<var>=<val1> if<condition> else <val2>
food=input("food: ")
eat ="yes" if food =="chanachor" else "no"
print(eat)
#or <stl1> if<condition> else <stl2>
print("Yes") if food=="chanachor" or food=="kacchi" else print("No")
#clever if / ternary operator
#<var>=(false_val,true_val) [<condition>]
age=int(input("age: "))
vote=("Yes","No") [age<18]
print(vote)
#or exa
sal=float(input("sal: "))
tax=sal*(0.1,0.2) [sal>5000]
print(tax)
#Operators
#type conversiuon(by defult in python) ,type casting(namuali conversion)
p="12"
q=int(p)
print(q)
g=234
h=str(g)
print(h)


