Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = {}
type(s)
<class 'dict'>
s=set()
s={1,2,3,4,12,324,9876,34,12431324}
s
{1, 2, 3, 4, 34, 324, 12, 9876, 12431324}
s
{1, 2, 3, 4, 34, 324, 12, 9876, 12431324}
s.set()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.set()
AttributeError: 'set' object has no attribute 'set'
s
{1, 2, 3, 4, 34, 324, 12, 9876, 12431324}
s.add(1)
s.add(12.3)
s.add(2+4j)
s.add()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s
{1, 2, 3, 4, 34, 324, 12, 12.3, (2+4j), 9876, 12431324}
s={1,1,1,1,1,1,1}
s
{1}
1={10,20,30}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l={10,20,30}
m={1,2,3,4}
l+m
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a = {1,2,3,4,5}
b = {3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a | b
{1, 2, 3, 4, 5, 7, 9}
a&b
{3, 5}
a - b
{1, 2, 4}
a^b
{1, 2, 4, 7, 9}
{1}<=a
True
{1,2,3,4}<=a
True
a
{1, 2, 3, 4, 5}
{,2,3,4,5}<=a
SyntaxError: invalid syntax
{1,2,3,4,5}<=a
True
b
{9, 3, 5, 7}
a.isdisjoint(b)
False
a.iddisjoint({9,10})
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.iddisjoint({9,10})
AttributeError: 'set' object has no attribute 'iddisjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issunset(b)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.issunset(b)
AttributeError: 'set' object has no attribute 'issunset'. Did you mean: 'issubset'?
a.issubset(b)
False
a
{1, 2, 3, 4, 5}
5 in a
True
7 in a
False
8 not in a
True
a
{1, 2, 3, 4, 5}
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
a.add(12)
a
{1, 2, 3, 4, 5, 12}
b.add(13)
b
{1, 2, 3, 4, 5, 12, 13}
c = a.copy()
c.add(12)
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12, 13}
a.add(123)
a
{1, 2, 3, 4, 5, 123, 12, 13}
a.update({16,17,18})
a
{1, 2, 3, 4, 5, 12, 13, 16, 17, 18, 123}
a.pop()
1
a.remove(16)
a
{2, 3, 4, 5, 12, 13, 17, 18, 123}
a.remove(12)
a
{2, 3, 4, 5, 13, 17, 18, 123}
a.discard(12)
a.discard(5)
a
{2, 3, 4, 13, 17, 18, 123}
a.clear()
a
set()
a={1,2,4,5}
a.update({"str,012,13,-1,-23.4})
          
SyntaxError: unterminated string literal (detected at line 1)
a.update({"Str",0,12,13,-1,-23.4})
          
a
          
{0, 1, 2, 4, 5, -23.4, 12, 13, 'Str', -1}
len(a)
          
10
all(a)
          
False
any(a)
          
True
a = frozenset({1,12,13,10,18,59,20})
          
a
          
frozenset({1, 18, 20, 10, 59, 12, 13})
a.add(12)
          
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
d={}
          
d=dict()
          
type(d)
          
<class 'dict'>
d = {'k1':'v1','k2':'v2','k3':'v3'}
          
d
          
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
          
1952819550976
d['k4'] = 'v4'
          
d
          
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d={}
          
d[1]='int'
          
d
          
{1: 'int'}
d[12.3]='flt'
          
d
          
{1: 'int', 12.3: 'flt'}
d[2+3j]='com'
          
d
          
{1: 'int', 12.3: 'flt', (2+3j): 'com'}
d['str']='string'
          
d
          
{1: 'int', 12.3: 'flt', (2+3j): 'com', 'str': 'string'}
d[(1,2,3,4)]='tuple'
          
d
          
{1: 'int', 12.3: 'flt', (2+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d={}
          
d[1]=1
          
d[2]=12.3
          
d[3]=12+4j
          
d[4]='str'
          
d[5]=[1,2,3,4]
          
d[6](1,2,3)
          
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    d[6](1,2,3)
KeyError: 6
d7]={1,2,3}
         
SyntaxError: unmatched ']'
d[7]={1,2,3}
         
d[8]={1:1}
         
d[9]=True
         
d
         
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 7: {1, 2, 3}, 8: {1: 1}, 9: True}
9 in d
         
True
10 in d
         
False
'str' in d
         
False
d[5]
         
[1, 2, 3, 4]
d[8]
         
{1: 1}
>>> d.get(10)
...          
>>> d.get(1)
...          
1
>>> d.get(10,"ket is not present")
...          
'ket is not present'
>>> d.get(6,"key is not present")
...          
'key is not present'
>>> d.get(5,"key is present")
...          
[1, 2, 3, 4]
>>> d[3]=4
...          
>>> d
...          
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[3]=4
...          
>>> d
...          
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[5]=10
...          
>>> d
...          
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[6]=12
...          
>>> d
...          
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 7: {1, 2, 3}, 8: {1: 1}, 9: True, 6: 12}
>>> d[7]=20
...          
>>> d
         
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 7: 20, 8: {1: 1}, 9: True, 6: 12}
