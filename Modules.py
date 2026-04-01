Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

================== RESTART: C:/Users/HP/Desktop/29/mymodule.py =================
#math module
import nath
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import nath
ModuleNotFoundError: No module named 'nath'
math.pi
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    math.pi
NameError: name 'math' is not defined. Did you forget to import 'math'?
import math
math.pi
3.141592653589793
math.pi*3
9.42477796076938
math.sqrt(2)
1.4142135623730951
math.pow(2,2)
4.0
math.log(10)
2.302585092994046
math.sin(60)
-0.3048106211022167
>>> math.cos(85)
-0.9843766433940419
>>> int(math(sin(60)))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int(math(sin(60)))
NameError: name 'sin' is not defined. Did you mean: 'bin'?
>>> math.tan(45)
1.6197751905438615
>>> math.ceil(5.9)
6
>>> math.florr(3.5)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    math.florr(3.5)
AttributeError: module 'math' has no attribute 'florr'. Did you mean: 'floor'?
>>> math.floor(3.6)
3
>>> math.ceil(2.7)
3
>>> math.ceil(0.1)
1
>>> math.ceil(6)
6
>>>  from math import pi,sqrt,log,pow
...  
SyntaxError: unexpected indent
>>> from math import pi,sqrt,log,pow
>>> pi
3.141592653589793
>>> sqrt(5)
2.23606797749979
>>> log(4)
1.3862943611198906
>>> pow(4,5)
1024.0

#System module (sys)
import sys



