Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> a = Tk()
>>> 
>>> b = b()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b = b()
NameError: name 'b' is not defined
>>> b=c()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b=c()
NameError: name 'c' is not defined
>>> c=Tk()
>>> 
>>> 
>>> print(c)
.
>>> 
>>> 
>>> a
<tkinter.Tk object .>
>>> c
<tkinter.Tk object .>
>>> print(a)
.
>>> return a
SyntaxError: 'return' outside function
>>> "
SyntaxError: EOL while scanning string literal
>>> ''
''
>>> a.title("second window")
''
>>> 
>>> a
<tkinter.Tk object .>
>>> c.title("third window")
''
>>> 