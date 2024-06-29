#day2
#chapter2 ( strings and conditions)
#strings
s1="strin1"
s2='String2'
s3="""Strin3"""
s4="i an richa,\n hello all"
print(s4)
#concatenation
s1+=s2
print(s2+s1)
#length of str
l=len(s4)
print(l)
fstr=s2+"    "+s3
print(fstr)
#indexing
ch=s4[5]
print(ch)
# not allow to do this s4[5]='a'
print(s4[4])
#Slicing use in string for ML 
"""accessing parts of a string.
str[starting_idx : ending_idx]  """
print(s4[2:7])
print(s4[2:])
print(s4[ :7])
#slicing negative index
"""A  p  p   l  e
   -5,-4,-3,-2,-1"""
ss="Apple"
print(ss[-3:-1])
#string Funtions
"""
1.str.endswith("le") -> retruns ture if string ends with substr
2.str.capitalize() -> capitaliuzes 1st char
3.str.replace(old,new) -> replaces all occurrences of old by new
4.str.find(word) -> retruns 1st index of 1st occurrer
5.str.count("pp") -> counts the occurrence of substr
"""
s2= s2.capitalize()
print(s2)
print(ss.endswith("le"))
print(ss.replace("pp","ee"))
print(ss)
print(ss.count("e"))
print(s4.find("all"))
#conditional statements
#indentation or poper space
#nesting
"""
if():
  if():
  else:
else :
"""
age=int(input("age: "))
if(age>=18):
    if(age<=80):
        print("Can do")
    else:
        print("risk")
else:
    print("Cant do")

if(age>=18 and age<=80) :
        print("Can do")
else:
    print("Cant do")
#chapter3 (Lists and tuples)
#Lists
"""
A build in data type stores of values.
It can store elements of different types(int,float,strinf)
"""
lt=[1,2,5,4,5,0,7,8,5]
print(lt)
print(type(lt))
print(len(lt))
print(lt[3])
lt[3]=3*3
print(lt[3])
#strings in python are immutable(not chage)
#lists in python are mutable(changable)
#list slicing similar to string
print(lt[3:9])
#list methods
"""
1.list.append(4) -> adds one element at the end
2.list.sort() -> sorts in ascending order
3.list.sort(reverse=Ture) ->sorts in descending order
4.list.reverse() -> reverse list
5.list.insert(idx,el) -> insert element at index
5.list.remove(1) -> removes first occurrence of element
6.list.pop(idx) -> removes element at index
"""
lt.append(10)
print(lt.append(100))
print(lt)
lt.sort()
print(lt)
vec=['d','r','e']
vec.reverse()
print(vec)
vec.insert(1,22)
vec.insert(1,9)
print(vec)
#python documentation search
#Tuples
"""
A built in data type that lets us create immutable sequences of values
tup=() or tup=(el,) or tup=(e1,e2,...)
"""
tup=(2,4,7,9,10)
print(type(tup))
print(tup)
t1=()
t2=(2)
t3=(2,)
print(type(t1), type(t2), type(t3))
#slicing in tuple as similar to string
print(tup[2:3])
#tuple methods
"""
1.tup.index(el) -> returns index of first occurrence
2.tup.count(el) 
"""
#chapter4 (Dictionary and Set)
#Dictionary
"""
Dictionaries are used to store data values in Key:Value pairs
They are unordered,mutable(changeable) and don't allow duplicate keys
"""
info={
     "key" : "value",
     "a" : "2",
     "b" : "3",
     "c" : 4,
     22: "Anika"
}
print(info)
print(type(info))
print(info[22])
info["a"]=9
print(info)
null_dict={}
null_dict['w']="Hello"
print(null_dict)
#Nested dictionary
std={
     "name" : "Anika",
     "sub":{
          "compiler" : 99,
          "AL":99,
          "GAN": 98,
          "Cryptograhpy" : 98
     }
}
print(std)
print(std["sub"])
print(std["sub"]["AL"])
#dictionary methods
"""
1.dict.key() -> retrunhs all keys
2.dicr.values() -> retrun all values
3.dict.intem() -> returns all (key,val) pairs as tuples
4.dict.get("key") -> returns the key according to value
5. dict.update(newdict) -> insert the sprcific items to the dict
"""
#type casting
print(list(std.keys()))
pairs=list(std.items())
print(pairs[1])
#print(std["Name"]) # error if not find
print(std.get("Name")) # none if not find
info.update(std)
print(info)













