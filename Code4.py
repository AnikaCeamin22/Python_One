#Day4
#chapter6 (functions and recursion)
#Recursion
"""
when a function calls itself repeatedly
def rec_name(parem1,param2,...):
    some work
    condition -> base case
    some work
rec_name(param1,param2,...)
"""
def Num(n):
    if(n==0):
         return
    print(n)
    Num(n-1)
    print("End")

Num(6)
#call stack -> recursion
def fact(n):
     if(n==0) :
          return 1
     return n*fact(n-1)
print(fact(5))
#chapter7 ( File i/o)
"""
python can used to perform oprations on a file.(read and write data)
Types of all files:
1.Text(character) files: .txt, .docx, .log ete
2.Binary Files: .mp4, .mov, .png, .jpeg etc

#open: we have to open a file before reading or writing.
f = open("file_name","mode")
file_name as sample.txt, demo.docx
mode as
       r: read mode(by default), write mode
#read:
data = f.read()
f.close()
"""
f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

f1 = open("demo.txt","r")
d=f1.read(20)
print(d)
f1.close()

f2 = open("demo.txt","r")
line1=f2.readline()
print(" line1: " +  line1)
line2=f2.readline()
print(" line2: " +  line2)
f2.close()

"""
#write:
f=open("demo.txt","w")
f.write("this is a new line") # overwrites the entire file
f=open("demo.txt","a")
f.write("this is a new line") # adds at th end to the file
"""
f=open("demo.txt","a")
f.write("\nthis is a new line on this file")
f.close()

f=open("sample.txt","a")
f.write("this is a new line\n")
f.close()

f=open("sample.txt","w")
f.write("ABCD chage")
f.close()

#with 
"""
whole process of file can write using "with"
with open("sample.txt,"a") as f:
   data=f.read()
"""
with open("sample.txt","r+") as f:
     data=f.read()
     print("data: " + data)
     f.write("\n hello all")
#no need to f.close() because with do it already
#deleting a file
"""
using the os module
module(like a code library) is a file written by another programmer that generally has a functions we can use.

import os 
os.remove("filename")
"""
import os
#os.remove("sample.txt")
#Exa: replace java with python
with open("sample.txt","w") as f:
    f.write("hi all\nwe are i/o\n using java\n")
with open("sample.txt","r") as f:
    data=f.read() # data string return
nd = data.replace("java","Python")
print(nd)
with open("sample.txt","w") as f:
    f.write(nd)

#EXA: find all word
word="all"
with open("sample.txt","r") as f:
     data=f.read()
     if(data.find(word)!=-1): # or word in data
          print("YES")
     else:
          print("NO") 
#EXa: find linnumber for a particular word
word="using"
data=True
num=1
with open("sample.txt","r") as f:
     while data:
        data=f.readline()
        #print(" line : " + data)
        if(word in data): # or word in data
          print(num)
          mun=-1
          break
        num+=1
if(num==-1):
    print(num)





