Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = 10
>>> A=20
>>> a
10
>>> A
20
>>> a=10
>>> a=b=c=10
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a
10
>>> b
20
>>> a,bb,a
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a,bb,a
NameError: name 'bb' is not defined. Did you mean: 'b'?
>>> a,b=b,a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'A'?
