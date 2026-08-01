Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
data = {'name': 'sajid','batch':63,'course':'PFS'}
data['name']
'sajid'
data['batch']
63
date['course']
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    date['course']
NameError: name 'date' is not defined. Did you mean: 'data'?
data['course']
'PFS'
63 in data
False
data.get('age','key is not present')
'key is not present'
date.get('course','key is not present')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    date.get('course','key is not present')
NameError: name 'date' is not defined. Did you mean: 'data'?
data.get('course','key is not present')
'PFS'
data['batch']=64
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS'}
data['skills']=['python','mysql','flask']
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data['age']=21
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21}
data.update({'phno':9876543210,'email':'sajid@gmail.com'})
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'sajid@gmail.com'}
data.pop('age')
21
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210, 'email': 'sajid@gmail.com'}
data.pop('phno')
9876543210
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'sajid@gmail.com'}
del data['name']
data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'sajid@gmail.com'}
data.popitem()
('email', 'sajid@gmail.com')
data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data.popitem()
('skills', ['python', 'mysql', 'flask'])
data
{'batch': 64, 'course': 'PFS'}
data.clear()
data
{}
data.key()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    data.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
data={'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210, 'email': 'sajid@gmail.com'}
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210, 'email': 'sajid@gmail.com'}
data.keys()
dict_keys(['name', 'batch', 'course', 'skills', 'phno', 'email'])
dat.values()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dat.values()
NameError: name 'dat' is not defined. Did you mean: 'data'?
data.values()
dict_values(['sajid', 64, 'PFS', ['python', 'mysql', 'flask'], 9876543210, 'sajid@gmail.com'])
data.items()
dict_items([('name', 'sajid'), ('batch', 64), ('course', 'PFS'), ('skills', ['python', 'mysql', 'flask']), ('phno', 9876543210), ('email', 'sajid@gmail.com')])
sorted(data)
['batch', 'course', 'email', 'name', 'phno', 'skills']
sorted(data,reverse=True)
['skills', 'phno', 'name', 'email', 'course', 'batch']
max(data)
'skills'
min(data)
'batch'
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210, 'email': 'sajid@gmail.com'}
>>> data['age']
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    data['age']
KeyError: 'age'
>>> data.get('age')
>>> data.setdefault('age',0)
0
>>> data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210, 'email': 'sajid@gmail.com', 'age': 0}
>>> data.setdefault('name','')
'sajid'
>>> data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210, 'email': 'sajid@gmail.com', 'age': 0}
>>> len(data)
7
>>> all(data)
True
>>> data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210, 'email': 'sajid@gmail.com', 'age': 0}
>>> a={1:1,2:2}
>>> b=a
>>> b[3]=3
>>> a
{1: 1, 2: 2, 3: 3}
>>> b
{1: 1, 2: 2, 3: 3}
>>> \
... c= a.copy()
>>> c[4]=4
>>> c
{1: 1, 2: 2, 3: 3, 4: 4}
>>> a
{1: 1, 2: 2, 3: 3}
>>> d=dict.fromkeys(["a","b"],0)
>>> d
{'a': 0, 'b': 0}
