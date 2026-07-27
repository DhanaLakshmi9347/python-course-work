Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c= 'strings.py'
c.startswith('str')
True
c.startswith('python')
False
c.endswith('python')
False
c.endsswith('py')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    c.endsswith('py')
AttributeError: 'str' object has no attribute 'endsswith'. Did you mean: 'endswith'?
c.endswith('py')
True
c.islower()
True
c.upper()
'STRINGS.PY'
c.isupper()
False
'PYTHONV13'.isupper()
True
c.isalpha()
False
c.isalnum()
False
's123'.isalnum()
True
's.123'.isalnum()
False
'                   '.isspace()
True
'h                  '.isspace()
False
'this is tittle'.istitle()
False
'This Is Title'.istitle()
True
'my@var'.isidentifier()
False
'my_var'.isidentifier()
True
1=[]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[]
l=list()
l=[1,12.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},{1:1}
   l
   
SyntaxError: '[' was never closed
l=[1,12.3,2+3j],'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},{1:1}
   
l
   
([1, 12.3, (2+3j)], 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, {1: 1})
l=[1,1,1,1,1]
   
l
   
[1, 1, 1, 1, 1]
tyer(1)
   
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    tyer(1)
NameError: name 'tyer' is not defined
type(1)
   
<class 'int'>
l=[1,2,3,4]
   
m=[5,6,7]
   
l+m
   
[1, 2, 3, 4, 5, 6, 7]
m*3
   
[5, 6, 7, 5, 6, 7, 5, 6, 7]
l
   
[1, 2, 3, 4]
>>> l[3]
...    
4
>>> 1[-1]
...    
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    1[-1]
TypeError: 'int' object is not subscriptable
>>> 1[3]
...    
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    1[3]
TypeError: 'int' object is not subscriptable
>>> l[-l]
...    
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    l[-l]
TypeError: bad operand type for unary -: 'list'
>>> l[-1]
...    
4
>>> 1[1:]
...    
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    1[1:]
TypeError: 'int' object is not subscriptable
>>> l[1:]
...    
[2, 3, 4]
>>> l[:2]
...    
[1, 2]
>>> l[::-2]
...    
[4, 2]
