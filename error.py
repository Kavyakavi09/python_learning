
# 1) Syntax error
"""
print "hello"
  File "<stdin>", line 1
    print "hello"
    ^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
"""
#  2) index error
"""
 l=[1,2,3]
>>> l[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
"""
# 3) ModuleNotFoundError
"""
import pds
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pds'
"""
# 1*) SyntaxError for key
"""
d={"num":"1",num1="2"}
  File "<stdin>", line 1
    d={"num":"1",num1="2"}
                    ^
SyntaxError: ':' expected after dictionary key
"""
# 4) KeyError
"""
>>> d={'1':"a",'2':"b"} 
>>> d[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
"""
# 5) ImportError
"""from math import cube
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'cube' from 'math' (unknown location)"""
# 6) StopIteration
""">>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration"""

# 7) TypeError
"""
>>> "12"+12
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
"""
# 8) ValueError
"""
>>> int("abc")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'abc'
"""
# 9) NameError
"""
>>> age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
"""
# 10) ZeroDivisionError
"""
 100/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
"""
# 11) IndentationError
# if(5>3):
# print("hi")
""" print("hi")
    ^
IndentationError: expected an indented block after 'if' statement on line 82"""
