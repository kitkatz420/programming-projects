Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> exit()
>>> print("hello world?)
      
SyntaxError: EOL while scanning string literal
>>> print("hello world?")
hello world?
>>> age="hobble"
>>> print(age)
hobble
>>> x, y, z = "total", "drama", "island"
>>> print(x)
total
>>> print(y)
drama
>>> print(z)
island
>>> print("total drama" + z)
total dramaisland
>>> tdi=(x+y+z)
>>> print(tdi)
totaldramaisland
>>> x= "python is"
>>> y= "awesome"
>>> z=  x + y
>>> print(z)
python isawesome
>>> x="python is "
>>> print(z)
python isawesome
>>> z= x + y
>>> print(z)
python is awesome
>>> x = 5
>>> y = 10
>>> print(x * y)
50
>>> x = "awesome"
>>> def myfunc():
	x = "fantastic"
	print("python is " + x)
	print(x)
myfunc()
SyntaxError: invalid syntax
>>> print(x)
awesome
>>> def myfunc()
SyntaxError: invalid syntax
>>> def myfunc():
	x = "fantastic"
	print(x)

	
>>> def myfunc():
	x = "fantastic"
	print(x)
	x= "fantastic"
	print(x)
	def myfunc():
		global x
		x = "fantastic"
		myfunc()

		
>>> myfunc()
fantastic
fantastic
>>> print("my dick is " + x)
my dick is awesome
>>> def myfunc():
	global x
	x = ("fantastic")
myfunc()
SyntaxError: invalid syntax
>>> 
>>> myfunc()
fantastic
fantastic
>>> print(x)
awesome
>>> x = 5
>>> print(type(x))
<class 'int'>
>>> x = 'hello world'
>>> print(type(x))
<class 'str'>
>>> x = 20.5
>>> print(type(x))
<class 'float'>
>>> x = 1j
>>> pritn(type(x))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    pritn(type(x))
NameError: name 'pritn' is not defined
>>> print(type(x))
<class 'complex'>
>>> x = ['apple', 'banana', 'cherry']
>>> print(type(x))
<class 'list'>
>>> x = range(6)
>>> print(type(x))
<class 'range'>
>>> {'name' : 'john', 'age' : 36}
{'name': 'john', 'age': 36}
>>> {"name" : "john", "age" : 36}
{'name': 'john', 'age': 36}
>>> x = {"name" : "john", "age" : 36}
>>> print(type(x))
<class 'dict'>
>>> x = true
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    x = true
NameError: name 'true' is not defined
>>> x = True
>>> print(type(x))
<class 'bool'>
>>> x = 1
>>> y = 2.8
>>> z = 1j
>>> 
>>> a = float(x)
>>> print(a)
1.0
>>> b = int(y)
>>> print(b)
2
>>> c = complex(z)
>>> print(c)
1j
>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'int'>
>>> print(type(c))
<class 'complex'>
>>> import random
>>> print(random.randrange(1,10))
7
>>> print(random.randrange(1,500))
325
>>> def myfunc():
	x = int(1)
	print(x)
	global
	
SyntaxError: invalid syntax
>>> def myfunc():
	global x
	x = int(1)
myfunc()
SyntaxError: invalid syntax
>>> a = int(1)
>>> b = int(2.8)
>>> c = int("3")
>>> print(a)
1
>>> print(b)
2
>>> print(c)
3
>>> 
>>> a = """ go fuck yourself you lil ass bitch boy."""
>>> print(a)
 go fuck yourself you lil ass bitch boy.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a = """i want to bang you babey"""
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print(a)
i want to bang you babey
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a = "hello world"
>>> print(a[1])
e
>>> print(a[0])
h
>>> print(a[0:5])
hello
>>> print(a[-5:-2])
wor
>>> print(len(a))
11
>>> print(a.strip())
hello world
>>> print(a.upper())
HELLO WORLD
>>> print(a.replace("h", "j"))
jello world
>>> print(a.split(" "))
['hello', 'world']
>>> a = (a.split(" "))
>>> print(a)
['hello', 'world']
>>> a = (a.replace("h" "j"))
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    a = (a.replace("h" "j"))
AttributeError: 'list' object has no attribute 'replace'
>>> a = (a.replace("h", "j"))
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    a = (a.replace("h", "j"))
AttributeError: 'list' object has no attribute 'replace'
>>> a = (a.upper(0))
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    a = (a.upper(0))
AttributeError: 'list' object has no attribute 'upper'
>>> a = (a.upper())
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    a = (a.upper())
AttributeError: 'list' object has no attribute 'upper'
>>> txt = "the rain in spain stays mainly in the plain"
>>> x = "ain" in txt
>>> print(x)
True
>>> x="ain" not in txt
>>> print(x)
False
>>> a="Hello"
>>> b="world"
>>> c=a+" "+b
>>> print(c)
Hello world
>>> age=36
>>> txt="my name is john, and i am {}"
>>> print(txt.format(age))
my name is john, and i am 36
>>> quantity=3
>>> itemno=567
>>> price=49.95
>>> myorder="I want {} pieces of item {} for {} dollars."
>>> print(myorder.format(quantity, itemno, price))
I want 3 pieces of item 567 for 49.95 dollars.
>>> myorder="i want to pay {2} dollars for {0} pieces of item {1}"
>>> print(myorder.fromat(quantity, itemno, price))
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    print(myorder.fromat(quantity, itemno, price))
AttributeError: 'str' object has no attribute 'fromat'
>>> print(myorder.format(quantity, itemno, price))
i want to pay 49.95 dollars for 3 pieces of item 567
>>> txt="we are the so-called \"vikings\" from the north."
>>> print(txt)
we are the so-called "vikings" from the north.
>>> txt="\110\145\154\154\157"
>>> print(txt)
Hello
>>> print(a)
Hello
>>> print(a.casefold())
hello
>>> print(a.endswith(3))
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    print(a.endswith(3))
TypeError: endswith first arg must be str or a tuple of str, not int
>>> print(a.encode())
b'Hello'
>>> print(a.endswith())
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    print(a.endswith())
TypeError: endswith() takes at least 1 argument (0 given)
>>> a=200
>>> b=33
>>> print("b is greater than a")
b is greater than a
>>> print(bool("hello"))
True
>>> print(bool(15))
True
>>> x="hello"
>>> y=15
>>> print(bool(x))
True
>>> print(bool(y))
True
>>> class myclass():
	def _len_(self):
		return 0
	myobj= myclass()
	print(bool(myobj))
	class myclass ():
		def _len_(self):
			return 0

Traceback (most recent call last):
  File "<pyshell#222>", line 1, in <module>
    class myclass():
  File "<pyshell#222>", line 4, in myclass
    myobj= myclass()
NameError: name 'myclass' is not defined
>>> class myclass():
	def _len_(self):
		return 0
myobj=myclass()
SyntaxError: invalid syntax
>>> def myFunction() :
	return True
print(myfunction())
SyntaxError: invalid syntax
>>> print(myFunction())
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    print(myFunction())
NameError: name 'myFunction' is not defined
>>> def myFunction() :
	return true
print(myFunction())
SyntaxError: invalid syntax
>>> def myFunction() :
	return True
print(myFunction())
SyntaxError: invalid syntax
>>> def myFunction():
	return True
print(myFunction())
SyntaxError: invalid syntax
>>> def myFunction():
	return True
if myFunction():
	
SyntaxError: invalid syntax
>>> print(myFunction)
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    print(myFunction)
NameError: name 'myFunction' is not defined
>>> print(10>9)
True
>>> x= 20
>>> y=20
>>> y is x
True
>>> thislist= ["apple", "banana", "cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> print(thislist[1])
banana
>>> print(thislist[3])
Traceback (most recent call last):
  File "<pyshell#252>", line 1, in <module>
    print(thislist[3])
IndexError: list index out of range
>>> print(thislist[-1])
cherry
>>> print(thislist[0])
apple
>>> thislist("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    thislist("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
TypeError: 'list' object is not callable
>>> thislist= ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
>>> print(thislist[2:5])
('cherry', 'orange', 'kiwi')
>>> print(thislist[:4])
('apple', 'banana', 'cherry', 'orange')
>>> print(thislist[2:])
('cherry', 'orange', 'kiwi', 'melon', 'mango')
>>> print(thislist[-4:-1])
('orange', 'kiwi', 'melon')
>>>   thislist[1]= "blackcurrant"
  
SyntaxError: unexpected indent
>>> thislist[1]= "blackcurrant"
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    thislist[1]= "blackcurrant"
TypeError: 'tuple' object does not support item assignment
>>> thislist[1] = "blackcurrant"
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    thislist[1] = "blackcurrant"
TypeError: 'tuple' object does not support item assignment
>>> thislist= ['apple','banana', 'cherry']
>>> for x in thislist
SyntaxError: invalid syntax
>>> for x in thislist:
	print(x)
	print(thislist)
	 for apple in thislist:
		 
SyntaxError: unexpected indent
>>> for x in thislist:
	print(apple)

	
Traceback (most recent call last):
  File "<pyshell#272>", line 2, in <module>
    print(apple)
NameError: name 'apple' is not defined
>>> if apple in thislist:
	print('yes')
	if "apple"
	
SyntaxError: invalid syntax
>>> print(randrange(5,6))
Traceback (most recent call last):
  File "<pyshell#276>", line 1, in <module>
    print(randrange(5,6))
NameError: name 'randrange' is not defined
>>> print(random.randrange(5,6))
5
>>>  thislist= ["apple", "banana", "cherry"]
 
SyntaxError: unexpected indent
>>> thislist= ["apple", "banana", "cherry"]
>>> thislist.append("orange")
>>> print(thislist)
['apple', 'banana', 'cherry', 'orange']
>>> thislist.append(1, "kiwi")
Traceback (most recent call last):
  File "<pyshell#282>", line 1, in <module>
    thislist.append(1, "kiwi")
TypeError: append() takes exactly one argument (2 given)
>>> thislist.insert(1, "kiwi")
>>> print(thislist)
['apple', 'kiwi', 'banana', 'cherry', 'orange']
>>> thislist.remove("kiwi")
>>> print(thislist)
['apple', 'banana', 'cherry', 'orange']
>>> thislist.pop()
'orange'
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> del thislist[0]
>>> print(thislist)
['banana', 'cherry']
>>> del (thislist)
>>> thislist= ("spple", "banana", "cherry")
>>> thislist.clear()
Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    thislist.clear()
AttributeError: 'tuple' object has no attribute 'clear'
>>> print(thislist)
('spple', 'banana', 'cherry')
>>> thislist.clear()
Traceback (most recent call last):
  File "<pyshell#295>", line 1, in <module>
    thislist.clear()
AttributeError: 'tuple' object has no attribute 'clear'
>>> thislist= ("apple", "banana", "cherry")
>>> thislist.clear()
Traceback (most recent call last):
  File "<pyshell#297>", line 1, in <module>
    thislist.clear()
AttributeError: 'tuple' object has no attribute 'clear'
>>> thislist= ["apple", "banana", "cherry"]
>>> thislist.clear()
>>> print(thislist)
[]
>>> thislist= ["apple", "banana", "cherry"]
>>> mylist= thislist.copy()
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> mylist.insert(1, "kiwi")
>>> print(mylist)
['apple', 'kiwi', 'banana', 'cherry']
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> melist= list(thislist)
>>> print(melist)
['apple', 'banana', 'cherry']
>>> melist.insert(2, "watermelon")
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> print(mylist)
['apple', 'kiwi', 'banana', 'cherry']
>>> print(melist)
['apple', 'banana', 'watermelon', 'cherry']
>>> list1= ("a", "b", "c")
>>> list2= [1, 2, 3]
>>> list1= ['a', 'b', 'c']
>>> list3= list1 + list2
>>> print(list3)
['a', 'b', 'c', 1, 2, 3]
>>> for x in list2:
	list1.append(x)
print(list1)
SyntaxError: invalid syntax
>>> list1= ['a']
>>> list2= [2]
>>> for x in list2:
	list1.append(x)

	
>>> print(list1)
['a', 2]
>>>  list1= ['a']
 
SyntaxError: unexpected indent
>>> list1= ["a"]
>>> list2= [1]
>>> list1.extend(list2)
>>> print(list1)
['a', 1]
>>> thislist= list(("apple", "banana", "cherry"))
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist.count()
Traceback (most recent call last):
  File "<pyshell#334>", line 1, in <module>
    thislist.count()
TypeError: count() takes exactly one argument (0 given)
>>> thislist.reverse()
>>> print(thislist)
['cherry', 'banana', 'apple']
>>> thislist.reverse()
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist.sort()
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist.sort(1)
Traceback (most recent call last):
  File "<pyshell#341>", line 1, in <module>
    thislist.sort(1)
TypeError: sort() takes no positional arguments
>>>   thistuple= ('apple', 'banana', 'cherry')
  
SyntaxError: unexpected indent
>>> thistuple= ("apple", "banana", "cherry")
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> print(thistuple[1])
banana
>>> print(thistuple[-1])
cherry
>>> print(thistuple[2:5])
('cherry',)
>>> thistuple= ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
>>> print(thistuple[2:5])
('cherry', 'orange', 'kiwi')
>>> print(thistuple[-4:-1])
('orange', 'kiwi', 'melon')
>>> x= ('apple', 'banana', 'cherry')
>>> y= list(x)
>>> y[1]= 'kiwi'
>>> x= tuple(y)
>>> print(x)
('apple', 'kiwi', 'cherry')
>>> insert.x('kiwi')
Traceback (most recent call last):
  File "<pyshell#356>", line 1, in <module>
    insert.x('kiwi')
NameError: name 'insert' is not defined
>>> insert.x('kiwi'[1])
Traceback (most recent call last):
  File "<pyshell#357>", line 1, in <module>
    insert.x('kiwi'[1])
NameError: name 'insert' is not defined
>>> x.insert("kiwi")
Traceback (most recent call last):
  File "<pyshell#358>", line 1, in <module>
    x.insert("kiwi")
AttributeError: 'tuple' object has no attribute 'insert'
>>> y= list(x)
>>> y[3]= 'peaches'
Traceback (most recent call last):
  File "<pyshell#360>", line 1, in <module>
    y[3]= 'peaches'
IndexError: list assignment index out of range
>>> insert.y('kiwi')
Traceback (most recent call last):
  File "<pyshell#361>", line 1, in <module>
    insert.y('kiwi')
NameError: name 'insert' is not defined
>>> insert.y('kiwi'[2])
Traceback (most recent call last):
  File "<pyshell#362>", line 1, in <module>
    insert.y('kiwi'[2])
NameError: name 'insert' is not defined
>>> x= tuple(y)
>>> thistuple= ('apple', 'banana', 'cherry')
>>> for x in thistuple:
	print(x)

	
apple
banana
cherry
>>> for x in thistuple:
	print(x)

	
apple
banana
cherry
>>> if 'apple' in thistuple:
	print('yes')

	
yes
>>> if 'cherry' in thistuple:
	print('yes')

	
yes
>>> print(len(thistuple))
3
>>> #this is a note
>>> mytuple= ('kiwi',)
>>> print(mytuple)
('kiwi',)
>>> del mytuple
>>> print(mytuple)
Traceback (most recent call last):
  File "<pyshell#391>", line 1, in <module>
    print(mytuple)
NameError: name 'mytuple' is not defined
>>> tuple1= ('a', 'b', 'c')
>>> tuple2=(1, 2, 3)
>>> tuple3= tiple1 + tuple2
Traceback (most recent call last):
  File "<pyshell#394>", line 1, in <module>
    tuple3= tiple1 + tuple2
NameError: name 'tiple1' is not defined
>>> tuple3= tuple1 + tuple2
>>> print(tuple3)
('a', 'b', 'c', 1, 2, 3)
>>> metuple= tuple(('apple', 'banana', 'cherry'))
>>> print(metuple)
('apple', 'banana', 'cherry')
>>> del thistuple
>>> del metuple
>>> del mytuple
Traceback (most recent call last):
  File "<pyshell#401>", line 1, in <module>
    del mytuple
NameError: name 'mytuple' is not defined
>>> del tuple3
>>> del tuple1
>>> del tuple2
>>> thisset= {'apple', 'banana', 'cherry'}
>>> print(thisset)
{'cherry', 'apple', 'banana'}
>>> for x in thisset:
	print(x)

	
cherry
apple
banana
>>> print('banana' in thisset)
True
>>> thisset.add('orange')
>>> print(thisset)
{'cherry', 'orange', 'apple', 'banana'}
>>> thisset.update(['kiwi', 'mango', 'grapes', 'pineapple'])
>>> print(thisset)
{'cherry', 'orange', 'pineapple', 'grapes', 'mango', 'kiwi', 'apple', 'banana'}
>>> thisset= {'apple', 'banana', 'cherry'}
>>> print(len(thisset))
3
>>> thisset.remove('banana')
>>> print()thisset
SyntaxError: invalid syntax
>>> print(thisset)
{'cherry', 'apple'}
>>> thisset= ('apple', 'banana', 'cherry')
>>> thisset.discard('banana')
Traceback (most recent call last):
  File "<pyshell#421>", line 1, in <module>
    thisset.discard('banana')
AttributeError: 'tuple' object has no attribute 'discard'
>>> thisset.discard('banana')
Traceback (most recent call last):
  File "<pyshell#422>", line 1, in <module>
    thisset.discard('banana')
AttributeError: 'tuple' object has no attribute 'discard'
>>> thisset={'apple', 'banana', 'cherry'}
>>> thisset.discard('banana')
>>> print(thisset)
{'cherry', 'apple'}
>>> thisset= {'apple', 'banana', 'cherry'}
>>> x= thisset.pop()
>>> print(x)
cherry
>>> print(thisset)
{'apple', 'banana'}
>>> thisset.clear()
>>> print(thisset)
set()
>>> thisset= {'apple', 'banana', 'cherry'}
>>> print(thisset)
{'cherry', 'apple', 'banana'}
>>> del thisset
>>> print(thisset)
Traceback (most recent call last):
  File "<pyshell#435>", line 1, in <module>
    print(thisset)
NameError: name 'thisset' is not defined
>>> set1= {'a', 'b', 'c'}
>>> set2= {1, 2, 3}
>>> set3= set1.union(set2)
>>> print(set3)
{1, 2, 3, 'b', 'c', 'a'}
>>> set1.update(set2)
>>> print(set1)
{1, 2, 3, 'b', 'c', 'a'}
>>> thisset= set(('booty', 'pirates', 'pussy'))
>>> print(thisset)
{'booty', 'pussy', 'pirates'}
>>> thisdict= { 'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> print(thisdict)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> x= thisdict['model']
>>> x= thisdict['mustang']
Traceback (most recent call last):
  File "<pyshell#447>", line 1, in <module>
    x= thisdict['mustang']
KeyError: 'mustang'
>>> x= thisdict.get("model")
>>> print(x)
mustang
>>> thisdict["year"]= 2018
>>> print(thisdict)
{'brand': 'ford', 'model': 'mustang', 'year': 2018}
>>> thisdict["year"]= 1964
>>> for x in thisdict:
	print(x)

	
brand
model
year
>>> for x in thisdict:
	print(thisdict[x])

	
ford
mustang
1964
>>> for x in thisdict.values():
	print(x)

	
ford
mustang
1964
>>> for x, y in thisdict.items():
	print(x, y)

	
brand ford
model mustang
year 1964
>>> if 'model' in thisdict:
	print('yes')

	
yes
>>> print(len(thisdict))
3
>>> thisdict['color']= 'red'
>>> print(thisdict)
{'brand': 'ford', 'model': 'mustang', 'year': 1964, 'color': 'red'}
>>> thisdict= { 'brand':'ford', 'model': 'mustang', 'year': 1964}
>>> thisdict.pop('model')
'mustang'
>>> print(thisdict)
{'brand': 'ford', 'year': 1964}
>>> thisdict['model']= 'mustang'
>>> print(thisdict)
{'brand': 'ford', 'year': 1964, 'model': 'mustang'}
>>> thisdict.popitem()
('model', 'mustang')
>>> print(thisdict)
{'brand': 'ford', 'year': 1964}
>>> thisdict['model']= 'mustang'
>>> print(thisdict)
{'brand': 'ford', 'year': 1964, 'model': 'mustang'}
>>> del thisdict['model']
>>> print(thisdict)
{'brand': 'ford', 'year': 1964}
>>> thisdict['model']= 'mustang'
>>> print(thisdict)
{'brand': 'ford', 'year': 1964, 'model': 'mustang'}
>>> del thisdict
>>> print(thisdict)
Traceback (most recent call last):
  File "<pyshell#485>", line 1, in <module>
    print(thisdict)
NameError: name 'thisdict' is not defined
>>> thisdict={'brand':'ford', 'model':'mustang', 'year':1964)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> thisdict={'brand':'ford', 'model':'mustang', 'year':1964}
>>> print(thisdict)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> thisdict.clear()
>>> print(thisdict)
{}
>>> thisdict={'brand':'ford', 'model':'mustang', 'year':1964}
>>> print(thisdict)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> mydict=thisdict.copy()
>>> print(mycopy)
Traceback (most recent call last):
  File "<pyshell#495>", line 1, in <module>
    print(mycopy)
NameError: name 'mycopy' is not defined
>>> print(mydict)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> myfamily= {'child1':{'name':'emil', 'year':2004},'child2':{'name':'tobias', 'year':2007}, 'child3':{'name':'linus', 'year':2011}}
>>> print(myfamily)
{'child1': {'name': 'emil', 'year': 2004}, 'child2': {'name': 'tobias', 'year': 2007}, 'child3': {'name': 'linus', 'year': 2011}}
>>> child1{'name':'emil', 'year':2004}
SyntaxError: invalid syntax
>>> child1={'name':'emil', 'year':2004}
>>> child2={'name':'tobias', 'year':2007}
>>> child3={'name':'linus', 'year':2011}
>>> mefamily={'child1':child1, 'child2':child2, 'child3':child3}
>>> print(mefamily)
{'child1': {'name': 'emil', 'year': 2004}, 'child2': {'name': 'tobias', 'year': 2007}, 'child3': {'name': 'linus', 'year': 2011}}
>>> print(myfamily)
{'child1': {'name': 'emil', 'year': 2004}, 'child2': {'name': 'tobias', 'year': 2007}, 'child3': {'name': 'linus', 'year': 2011}}
>>> thisdict= dict(brand='ford', model='mustang', year=1964)
>>> print(thisdict)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> a=33
>>> b=200
>>> if b>a:
	print('yes')

	
yes
>>> if b>a:
	print('yes')

	
yes
>>> if b>a:
print('yes')
SyntaxError: expected an indented block
>>> a= 33
>>> b= 33
>>> if b>a:
	print('yes')

	
>>> elif a==b:
	
SyntaxError: invalid syntax
>>> elif a == b:
	
SyntaxError: invalid syntax
>>> if b>a:
	print('yes')

	
>>> if a==b:
	print('yes')

	
yes
>>> elif a == b:
	
SyntaxError: invalid syntax
>>> a=200
>>> b=33
>>> if b>a:
	print('yes greater')
	elif a==b:
		
SyntaxError: invalid syntax
>>> if b>a:
	print('yes yes yes')
elif a==b:
	print('ab equal')
else:
	print('a>b')

	
a>b
>>> if b>a:
	print('b>a')
elif b<a:
	print('b<a')

	
b<a
>>> if a>b: print('yes')

yes
>>> a=2
>>> b=330
>>> print('a') if a>b else print('b')
b
>>>  a=330
 
SyntaxError: unexpected indent
>>> b=330
>>> a=330
>>> print('a') if a>b else print('=') if a==b else print('b')
=
>>> a= 200
>>> b=33
>>> c=500
>>> if a>b and c>a:
	print('true')

	
true
>>> if a>b or a>c:
	print('at least one of the conditions is true')

	
at least one of the conditions is true
>>> x=41
>>> if x>10:
	print('above ten,')
	if x>20:
		print('and also above 20')
		else:
			
SyntaxError: invalid syntax
>>> if x>10:
	print('above ten')
	if x>20:
		print('also above 20')
	else:
		print('but not above 20')

		
above ten
also above 20
>>> a=33
>>> b=200
>>> if b>a:
	pass

>>> i= 1
>>> while i>6:
	print(i)
	i += 1

	
>>> while i<6:
	print(i)
	i += 1

	
1
2
3
4
5
>>> while i<6:
	print(i)
	if i==3:
		break
	i+=1

	
>>> i=0
>>> while i<6:
	i+=1
	if i==3:
		continue
	print(i)

	
1
2
4
5
6
>>> i=1
>>> while i<6:
	print(i)
	i+=1
else:
	print('i is no longer less than 6')

	
1
2
3
4
5
i is no longer less than 6
>>> fruits= ['apple', 'banana', 'cherry']
>>> for x in furits:
	print(x)

	
Traceback (most recent call last):
  File "<pyshell#618>", line 1, in <module>
    for x in furits:
NameError: name 'furits' is not defined
>>> for x in fruits:
	print(x)

	
apple
banana
cherry
>>> for x in 'banana':
	print(x)

	
b
a
n
a
n
a
>>> for x in fruits:
	print(x)
	if x=='banana':
		break

	
apple
banana
>>> for x in fruits:
	print(x)

	
apple
banana
cherry
>>> for x in fruits:
	print(x)

	
apple
banana
cherry
>>> for x in fruits:
	if x=='banana':
		break
	print(x)

	
apple
>>> for x in fruits:
	if x=='banana':
		continue
	print(x)

	
apple
cherry
>>> for x in range(6):
	print(x)

	
0
1
2
3
4
5
>>> for x in range(2:5):
	
SyntaxError: invalid syntax
>>> print(x)
5
>>> for x in range(2, 6):
	print(x)

	
2
3
4
5
>>> for x in range(2, 30, 3):
	print(x)

	
2
5
8
11
14
17
20
23
26
29
>>> for x in range(2, 30, 2):
	print(x)

	
2
4
6
8
10
12
14
16
18
20
22
24
26
28
>>> for x in range(30, 5):
	print(x)

	
>>> for x in range(1, 30, 5):
	print(x)

	
1
6
11
16
21
26
>>> for x in range(0, 30, 5):
	print(x)

	
0
5
10
15
20
25
>>> for x in range(6):
	print(x)
else:
	print('done')

	
0
1
2
3
4
5
done
>>> adj=['red', 'big', 'tasty']
>>> for x in adj:
	for y in fruits:
		print(x, y)

		
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
>>> for x in [0, 1, 2]:
	pass

>>> def my_function():
	print('hello from a function')

	
>>> my_function()
hello from a function
>>> def function_1():
	print('i love you bitch, aint never gonna stop loving you bitch')

	
>>> def my_function(fname):
	print(fname+'refsnes')

	
>>> my_function('emil')
emilrefsnes
>>> my_function('tobias')
tobiasrefsnes
>>> def my_function(fname):
	print(fname+' refsnes')

	
>>> my_function('emil')
emil refsnes
>>> my_function('tobias')
tobias refsnes
>>> my_function('linus')
linus refsnes
>>> def my_function(fname+' '+lname):
	
SyntaxError: invalid syntax
>>> def my_function(fname, lname):
	print(fname+' '+lname)
my_function('emil', 'refsnes')
SyntaxError: invalid syntax
>>> my_function('emil', 'refsnes')
Traceback (most recent call last):
  File "<pyshell#715>", line 1, in <module>
    my_function('emil', 'refsnes')
TypeError: my_function() takes 1 positional argument but 2 were given
>>> def function(fname, lname):
	print(fname+" "+ lname)
function('emil', 'refsnes')
SyntaxError: invalid syntax
>>> def function(fname, lname):
	print(fname + " " + lname)

	
>>> function('emil', 'refsnes')
emil refsnes
>>> def function(*kids):
	print('the youngest child is '+ kids[2])

	
>>> function('emil', 'tobias', 'linus')
the youngest child is linus
>>> def function(child3, child2, child1):
	print('the youngest child is '+child3)

	
>>> function(child1='emil', child2='tobias', child3='linus')
the youngest child is linus
>>> def function(**kid):
	print('his last name is '+ kid['lname'])

	
>>> function(fname= 'tobias', lname= 'refsnes')
his last name is refsnes
>>> def function(country='norway'):
	print('i am from '+ country)

	
>>> function()
i am from norway
>>> function('sweden')
i am from sweden
>>> function('india')
i am from india
>>> function()
i am from norway
>>> function('brazil')
i am from brazil
>>>  def function(food):
	 
SyntaxError: unexpected indent
>>> def function(food):
	for x in food:
		print(x)

		
>>> function(fruits)
apple
banana
cherry
>>> def function(x):
	return 5 * x
print(function(3))
SyntaxError: invalid syntax
>>> print(function(3))
Traceback (most recent call last):
  File "<pyshell#753>", line 1, in <module>
    print(function(3))
  File "<pyshell#748>", line 2, in function
    for x in food:
TypeError: 'int' object is not iterable
>>> def function(x):
	return 5*x

>>> print(function(3))
15
>>> print(function(5))
25
>>> pritn(function(9))
Traceback (most recent call last):
  File "<pyshell#759>", line 1, in <module>
    pritn(function(9))
NameError: name 'pritn' is not defined
>>> print(function(9))
45
>>> def function():
	pass

>>> function
<function function at 0x016BF5C8>
>>> def tri_recursion(k):
	if(k>0):
		result= k+tri_recursion(k-1)
		print(result)
	else:
		result= 0
		return = 0
	
SyntaxError: invalid syntax
>>> def recursion(k):
	if(k>0):
		result= k+recursion(k-1)
		print(result)
	else:
		result= 0
		return result

	
>>> print('\n\nRecursion Example Results')


Recursion Example Results
>>> recursion(6)
1
Traceback (most recent call last):
  File "<pyshell#781>", line 1, in <module>
    recursion(6)
  File "<pyshell#779>", line 3, in recursion
    result= k+recursion(k-1)
  File "<pyshell#779>", line 3, in recursion
    result= k+recursion(k-1)
  File "<pyshell#779>", line 3, in recursion
    result= k+recursion(k-1)
  [Previous line repeated 2 more times]
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> def recursion(k):
	if (k>0):
		result= k + recursion(k-1)
		print(result)
	else:
		result=0
		return result
print('\n\nrecursion example results')
SyntaxError: invalid syntax
>>> recursion(6)
1
Traceback (most recent call last):
  File "<pyshell#790>", line 1, in <module>
    recursion(6)
  File "<pyshell#779>", line 3, in recursion
    result= k+recursion(k-1)
  File "<pyshell#779>", line 3, in recursion
    result= k+recursion(k-1)
  File "<pyshell#779>", line 3, in recursion
    result= k+recursion(k-1)
  [Previous line repeated 2 more times]
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> function1()
Traceback (most recent call last):
  File "<pyshell#791>", line 1, in <module>
    function1()
NameError: name 'function1' is not defined
>>> myfunction()
Traceback (most recent call last):
  File "<pyshell#792>", line 1, in <module>
    myfunction()
NameError: name 'myfunction' is not defined
>>> my_function()
Traceback (most recent call last):
  File "<pyshell#793>", line 1, in <module>
    my_function()
TypeError: my_function() missing 1 required positional argument: 'fname'
>>> myfunction()
Traceback (most recent call last):
  File "<pyshell#794>", line 1, in <module>
    myfunction()
NameError: name 'myfunction' is not defined
>>> function_1
<function function_1 at 0x016BF460>
>>> function_1()
i love you bitch, aint never gonna stop loving you bitch
>>> x= lambda a : a+10
>>> print(x(5))
15
>>> x= lambda a, b:a*b
>>> print(x(5,6))
30
>>> x= lambda a, b, c:a+b+c
>>> print(x(5, 6, 6))
17
>>> def func(n):
	return lambda a:a*n

>>> doubler=func(2)
>>> print(doubler(11))
22
>>> print(doubler(22))
44
>>> quad=func(4)
>>> print(quad(4))
16
>>> triple=func(3)
>>> print(triple(4))
12
>>> cars=['ford', 'volvo', 'bmw']
>>> car1='ford'
>>> car2='volvo'
>>> car3'bmw'
SyntaxError: invalid syntax
>>> car3='bmw'
>>> x=cars[0]
>>> cars[0]='toyota'
>>> x=len(cars)
>>> print(x)
3
>>> x=cars[0]
>>> print(x)
toyota
>>> for x in cars:
	print(x)

	
toyota
volvo
bmw
>>> cars.append('honda')
>>> for x in cars:
	print(x)

	
toyota
volvo
bmw
honda
>>> cars.pop(0)
'toyota'
>>> for x in cars:
	print(x)

	
volvo
bmw
honda
>>> cars.remove('volvo')
>>> print(cars)
['bmw', 'honda']
>>> cars.append('volvo')
>>> print(cars)
['bmw', 'honda', 'volvo']
>>> car=('chevy', 'volkswagon', 'jeep')
>>> cars.extend(car)
>>> print(cars)
['bmw', 'honda', 'volvo', 'chevy', 'volkswagon', 'jeep']
>>> class class1:
	x=1

	
>>> print(class1)
<class '__main__.class1'>
>>> print(x)
honda
>>> p1=class1()
>>> print(p1.x)
1
>>> class person:
	def _init_(slef, name, age):
		self.name=name
		self.age=age

		
>>> p1=person('john', 36)
Traceback (most recent call last):
  File "<pyshell#858>", line 1, in <module>
    p1=person('john', 36)
TypeError: person() takes no arguments
>>> p1= person('john', 36)
Traceback (most recent call last):
  File "<pyshell#859>", line 1, in <module>
    p1= person('john', 36)
TypeError: person() takes no arguments
>>> class Person:
	self.name=name
	slef.age=age

	
Traceback (most recent call last):
  File "<pyshell#863>", line 1, in <module>
    class Person:
  File "<pyshell#863>", line 2, in Person
    self.name=name
NameError: name 'name' is not defined
>>> class Person:
	def_init_(self, name, age):
		
SyntaxError: invalid syntax
>>> class Person:
	def _init_(slef, name, age)
	
SyntaxError: invalid syntax
>>> def Person
SyntaxError: invalid syntax
>>> def Person:
	
SyntaxError: invalid syntax
>>> def _init_(self, name, age):
	self.name=name
	self.age=age

	
>>> p1=Person('john', 36)
Traceback (most recent call last):
  File "<pyshell#874>", line 1, in <module>
    p1=Person('john', 36)
NameError: name 'Person' is not defined
>>> p1 = Person("john", 36)
Traceback (most recent call last):
  File "<pyshell#875>", line 1, in <module>
    p1 = Person("john", 36)
NameError: name 'Person' is not defined
>>> class person:
	def _init_(self, name, age):
		self.name=name
		self.age=age
p1=person('john', 36)
SyntaxError: invalid syntax
>>> 
>>> p1= Person('john', 36)
Traceback (most recent call last):
  File "<pyshell#882>", line 1, in <module>
    p1= Person('john', 36)
NameError: name 'Person' is not defined
>>> class Person:
	def _init_(self, name, age):
		self.name = name
		self.age = age

		
>>> p1 = Person('john', 36)
Traceback (most recent call last):
  File "<pyshell#888>", line 1, in <module>
    p1 = Person('john', 36)
TypeError: Person() takes no arguments
>>> p1 = Person("john", 36)
Traceback (most recent call last):
  File "<pyshell#889>", line 1, in <module>
    p1 = Person("john", 36)
TypeError: Person() takes no arguments
>>> p1 = Person("John", 36)
Traceback (most recent call last):
  File "<pyshell#890>", line 1, in <module>
    p1 = Person("John", 36)
TypeError: Person() takes no arguments
>>> class person:
	def __init__(self, name, age):
		self.name=name
		self.age=age

		
>>> p1=person('john', 36)
>>> print(p1.name)
john
>>> print(p1.age)
36
>>> class person:
	def __init__(sillyobject, name, age):
		sillyobject.name=name
		sillyobject.age=age

		
>>> class person:
	def __init__(sillyobject, name, age):
		sillyobject.name=name
		sillyobject.age=age
	def func(abc):
		print('hello my name is '+abc.name)

		
>>> p1=person('john', 36)
>>> p1.func()
hello my name is john
>>> p1.age=40
>>> del p1.age
>>> del p1
>>> class person:
	pass

>>> class person:
	def __init__(self, name, age):
		self.firstname=fname
		self.lastname=lname
	def printname(self):
		print(self.firstname, self.lastname)

		
>>> x=person('john', 36)
Traceback (most recent call last):
  File "<pyshell#923>", line 1, in <module>
    x=person('john', 36)
  File "<pyshell#922>", line 3, in __init__
    self.firstname=fname
NameError: name 'fname' is not defined
>>> x.printname()
Traceback (most recent call last):
  File "<pyshell#924>", line 1, in <module>
    x.printname()
AttributeError: 'str' object has no attribute 'printname'
>>> x=person("john", 36)
Traceback (most recent call last):
  File "<pyshell#925>", line 1, in <module>
    x=person("john", 36)
  File "<pyshell#922>", line 3, in __init__
    self.firstname=fname
NameError: name 'fname' is not defined
>>> x=person('john', 36)
Traceback (most recent call last):
  File "<pyshell#926>", line 1, in <module>
    x=person('john', 36)
  File "<pyshell#922>", line 3, in __init__
    self.firstname=fname
NameError: name 'fname' is not defined
>>> class person:
	def __init__(self, fname, lname):
		self.firstname=fname
		self.lastname=lname

		
>>> def printname(self):
	print(self.firstname, self.lastname)

	
>>> x=person('john', 'doe')
>>> x.printname()
Traceback (most recent call last):
  File "<pyshell#936>", line 1, in <module>
    x.printname()
AttributeError: 'person' object has no attribute 'printname'
>>> class person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)

		
>>> x = person("john", "doe")
>>> x.printname()
john doe
>>> class student(person):
	pass

>>> print(student)
<class '__main__.student'>
>>> x=student('mike', 'olsen')
>>> x.printname()
mike olsen
>>> class student(person):
	def __init__(self, fname, lname):
		person.__init__(self, fname, lname)

		
>>> class student(person):
	def __init__(self, fname, lname):
		seuper().__init__(fname, lname)

		
>>> class student(person):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)
		self.graduationyear=2019

		
>>> x=student('mike', 'olsen', 2019)
Traceback (most recent call last):
  File "<pyshell#966>", line 1, in <module>
    x=student('mike', 'olsen', 2019)
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> class student(person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear=year

		
>>> x=student("mike", "olsen", 2019)
>>> def welcome(self):
	print('welcome', self.firstname, self.lastname, 'to the class of', self.graduationyear)

	
>>> x.printname(student)
Traceback (most recent call last):
  File "<pyshell#976>", line 1, in <module>
    x.printname(student)
TypeError: printname() takes 1 positional argument but 2 were given
>>> x.printname(x)
Traceback (most recent call last):
  File "<pyshell#977>", line 1, in <module>
    x.printname(x)
TypeError: printname() takes 1 positional argument but 2 were given
>>> tuple1= ('apple', 'banana', 'cherry')
>>> myit= iter(tuple1)
>>> print(next(myit))
apple
>>> print(next(myit))
banana
>>> print(next(myit))
cherry
>>> mystr= 'banana'
>>> myit= iter(mystr)
>>> print(next(myit))
b
>>> print(next(myit))
a
>>> print(next(myit))
n
>>> print(next(myit))
a
>>> print(next(myit))
n
>>> print(next(myit))
a
>>> for x in mytuple:
	print(x)

	
Traceback (most recent call last):
  File "<pyshell#993>", line 1, in <module>
    for x in mytuple:
NameError: name 'mytuple' is not defined
>>> for x in tuple1:
	print(x)

	
apple
banana
cherry
>>> for x in mystr:
	print(x)

	
b
a
n
a
n
a
>>> class number1:
	def __inter__(self):
		self.a=1
		return self

	
>>> class number1:
	def __inter__(self):
		self.a=1
		return self
	def __next__(self):
		x=self.a
		self.a+=1
		return x

	
>>> myclass=number1()
>>> myiter=iter(myclass)
Traceback (most recent call last):
  File "<pyshell#1012>", line 1, in <module>
    myiter=iter(myclass)
TypeError: 'number1' object is not iterable
>>> class MyNumbers:
	def __iter__(self):
		self.a=1
		return self
	def __next__(self):
		x=self.a
		self.a+=1
		return x

	
>>> myclass=MyNumbers()
>>> myiter=iter(myclass)
>>> print(next(myiter))
1
>>> print(next(myiter))
2
>>> print(next(myiter))
3
>>> print(next(myiter))
4
>>> print(next(myiter))
5
>>> print(next(myiter))
6
>>> print(next(myiter))
7
>>> print(next(myiter))
8
>>> class mynumbers:
	def __iter__(self):
		self.a=1
		return self
	def __next__(self):
		if self.a<=20:
			x=self.a
			self.a+=1
			return x
		else:
			raise StopIteration

		
>>> myclass=mynumbers()
>>> myiter=iter(myclass)
>>> for x in myiter:
	print(x)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
>>> def func():
	x=300
	print(x)

	
>>> func()
300
>>> def func():
	x=300
	def myinnerfunc():
		print(x)
	myinnerfunc()

	
>>> myfunc()
fantastic
fantastic
>>> func()
300
>>> x=300
>>> def func():
	print(x)

	
>>> func()
300
>>> print(x)
300
>>> x=300
>>> def func():
	x=200
	print(x)

	
>>> func()
200
>>> print(x)
300
>>> def func():
	global x
	x=300

	
>>> func()
>>> print(x)
300
>>> x=300
>>> def func():
	global x
	x=200

	
>>> func()
>>> print(x)
200
>>> 