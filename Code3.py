#Day3
#chapter4 ( Dictionary and set)
#set
"""
set is the collection of the unordered items.
each element in the set must be unique and immutable.
set can work with boolean,int,float,string,tuple. not work with list,dictionary.
"""
st={1,2,3,4,5,2,2,'a','a','r','c'}
print(st)
print(type(st))
print(len(st))
dt={} #empty dictionary
st=set() # empty set
print(type(st),type(dt))
#set methods
"""
1.st.add(el) ->adds an element
2.st.remove(el) -> removes the element
3.st.clear() -> empties the set
4.st.pop() -> removes a random value
5.st.union(st2) ->combines both set
6.st.intersection(st2) ->combines common 
"""
#sets mutable but set's elements are immutable
st.add(2)
st.add(22)
print(st)
st.add((1,3,6))
#st.add({2,5,9})
print(st)
st.pop()
print(st)
s2={'a','b','c',22}
print(st.intersection(s2))
#chapter5 ( Loops)
"""
Loops are used for sequential traversal. For traversing list,string,tuples etc.
while Loops:
   while condition:
      some work
For Loops:
   for el in list:
       some work
For loop with else
   for el in list:
      some work
    else
       work when loop end
"""
# break, continue
cnt=0
while cnt<5:
    print(cnt)
    cnt+=1
lt=[1,4,9,16,25,36]
i=0
x=16
while i<len(lt):
  if(lt[i]==x):
       print(lt[i])
       break
  i+=1

for i in lt:
    print(i)
s="ANIUKA"
for ch in s:
    if(ch=="U"):
        break
    print(ch)
else:
    print("END")
#range()
"""
Range function returns a sequence of numbers,starting from ) by default, and incerments by !(by default), and stops before a specified number.
range(start?,stop,step?)
"""
sq=range(7)
print(sq[3])
for i in range(3,10,2):
    print(i,end=" ")
#pass
"""
Pass is a null statement that does nothing.it is used as a placeholder for future code.
"""
for i in range(10):
    pass
cnt=0

if(cnt>5):
    pass
print(range(-2,3,-1))
#chapter6 (Functions and recursion)
#Functions
"""
Function is block of statements that perform a specific task.
def func_name(param1,param2,...):
   some work
   return val

func_name(ag1,ag2....) -> function call
"""
def fun(a,b,c):
    return a*b/c
print(fun(10,20,5),end=" ")
print(fun(20,3,9))
#Default parameters
def fun(a=1,b=2,c=1):
    return a*b/c

print(fun(),end=" ")
print(fun(20,3,9))


