Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sys module
import sys
sys.path
['', 'C:\\Users\\HP\\Desktop\\29', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']
sys.version
'3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)]'
for i in sys.path:
    print(i)

    

C:\Users\HP\Desktop\29
C:\Users\HP\AppData\Local\Programs\Python\Python313\python313.zip
C:\Users\HP\AppData\Local\Programs\Python\Python313\DLLs
C:\Users\HP\AppData\Local\Programs\Python\Python313\Lib
C:\Users\HP\AppData\Local\Programs\Python\Python313
C:\Users\HP\AppData\Local\Programs\Python\Python313\Lib\site-packages

#OS
import OS
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    import OS
ModuleNotFoundError: No module named 'OS'
import os
os.path
<module 'ntpath' (frozen)>
ps.getcwd()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ps.getcwd()
NameError: name 'ps' is not defined. Did you mean: 'os'?
>>> os.getcwd()
'C:\\Users\\HP\\Desktop\\29'
>>> os.listdr()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    os.listdr()
AttributeError: module 'os' has no attribute 'listdr'. Did you mean: 'listdir'?
>>> os.listdir()
['anonymous functions.py', 'Arguments1.py', 'Arguments2.py', 'Built in functions.py', 'Conditions.py', 'conditions2.py', 'Data types.py', 'data.py', 'data.txt', 'Dictionary.py', 'Dictionary2.py', 'File handling.py', 'Functions.py', 'Global and Local variable.py', 'Harika.txt', 'If else conditions.py', 'Inheritance.py', 'List comprehension.py', 'list.py', 'Loops 2.py', 'loops tasks.py', 'Loops.py', 'Modules.py', 'modules2.py', 'mymodule.py', 'Nested In.py', 'Oops.py', 'polymorphism methods.py', 'Polymorphism.py', 'Practice.py', 'run-time Input.py', 'Sets.py', 'strings.py', 'task 28th feb.py', 'Tuple.py', 'Variables.py', '__pycache__']
>>> 
>>> os.chdir()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    os.chdir()
TypeError: chdir() missing required argument 'path' (pos 1)
>>> os.chdir("C:\\Users\\HP\\Desktop\\29")
>>> os.listdir()
['anonymous functions.py', 'Arguments1.py', 'Arguments2.py', 'Built in functions.py', 'Conditions.py', 'conditions2.py', 'Data types.py', 'data.py', 'data.txt', 'Dictionary.py', 'Dictionary2.py', 'File handling.py', 'Functions.py', 'Global and Local variable.py', 'Harika.txt', 'If else conditions.py', 'Inheritance.py', 'List comprehension.py', 'list.py', 'Loops 2.py', 'loops tasks.py', 'Loops.py', 'Modules.py', 'modules2.py', 'mymodule.py', 'Nested In.py', 'Oops.py', 'polymorphism methods.py', 'Polymorphism.py', 'Practice.py', 'run-time Input.py', 'Sets.py', 'strings.py', 'task 28th feb.py', 'Tuple.py', 'Variables.py', '__pycache__']
>>> os.mkdir("april")
>>> os.listdir()
['anonymous functions.py', 'april', 'Arguments1.py', 'Arguments2.py', 'Built in functions.py', 'Conditions.py', 'conditions2.py', 'Data types.py', 'data.py', 'data.txt', 'Dictionary.py', 'Dictionary2.py', 'File handling.py', 'Functions.py', 'Global and Local variable.py', 'Harika.txt', 'If else conditions.py', 'Inheritance.py', 'List comprehension.py', 'list.py', 'Loops 2.py', 'loops tasks.py', 'Loops.py', 'Modules.py', 'modules2.py', 'mymodule.py', 'Nested In.py', 'Oops.py', 'polymorphism methods.py', 'Polymorphism.py', 'Practice.py', 'run-time Input.py', 'Sets.py', 'strings.py', 'task 28th feb.py', 'Tuple.py', 'Variables.py', '__pycache__']
