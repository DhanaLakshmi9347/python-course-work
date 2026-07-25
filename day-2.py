Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s=''
>>> s
''
>>> s='codegnan'
>>> s
'codegnan'
>>> 'codegnan' + 'PFS'
'codegnanPFS'
>>> 'codegnan'*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
>>> '_ *_'*20
'_ *__ *__ *__ *__ *__ *__ *__ *__ *__ *__ *__ *__ *__ *__ *__ *__ *__ *__ *__ *_'
>>> '*'*10
'**********'
>>> s = 'codegnan'
>>> s[4]
'g'
>>> s[-1]
'n'
>>> s[1]
'o'
>>> s[-2]
'a'
>>> names = 'dhana dimple subbu charan'
>>> name[0]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    name[0]
NameError: name 'name' is not defined. Did you mean: 'names'?
>>> names = 'dhana dimple subbu charan'
>>> names[0]
'd'
>>> names[6]
'd'
>>> 
>>> names[-1]
'n'
>>> #s[start:end+1:step]=>s[0:len:1]
>>> names[0:5]
'dhana'
names[:5}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
names[:5]
'dhana'
names
'dhana dimple subbu charan'
names[6:11]
'dimpl'
name[12:20]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    name[12:20]
NameError: name 'name' is not defined. Did you mean: 'names'?
names[12:20]
' subbu c'
names[21:]
'aran'
names[-1:-8:-1]
'narahc '
names[-9:-8:-1]
''
names[::2]
'daadml ub hrn'
names
'dhana dimple subbu charan'
'dhana'in names
True
'dimple'in names
True
'subbu' in names
True
