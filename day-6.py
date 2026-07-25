Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c = 'python programmig'
len (c)
17
ord('p')
112
ord('a')
97
ord('0')
48
ord('A')
65
chr(65)
'A'
chr(66)
'B'
min(c)
' '
max(c)
'y'
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
c= 'String id immutable'

c
'String id immutable'
c.upper()
'STRING ID IMMUTABLE'
c.lower()
'string id immutable'
c.capitalize()
'String id immutable'
c.title()
'String Id Immutable'
c.swapcase()
'sTRING ID IMMUTABLE'
'STRABEMALAGAANGST'.casefold()
'strabemalagaangst'
c
'String id immutable'
c.center(60,'_')
'____________________String id immutable_____________________'
c.center(60,'*')
'********************String id immutable*********************'
c.center(60,'0')
'00000000000000000000String id immutable000000000000000000000'
c.1just(60,'_')
SyntaxError: invalid imaginary literal
c.ijust(60,'_')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c.ijust(60,'_')
AttributeError: 'str' object has no attribute 'ijust'. Did you mean: 'ljust'?
c.ljust(60,'_')
'String id immutable_________________________________________'
c.rjust(60,'_')
'_________________________________________String id immutable'
'12'.zfill(4)
'0012'
c.find('s')
-1
c.find('i')
3
c.rfind('z')
-1
c.rfind('i')
10
c
'String id immutable'
c.index('i')
3
c.rindex('i')
10
c.index('z')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    c.index('z')
ValueError: substring not found
c
'String id immutable'
c.count('g')
1
c.count('m')
2
c
'String id immutable'
\
  c.replace('i','0')
SyntaxError: unexpected indent
c.replace('i','0')
'Str0ng 0d 0mmutable'
c.replace('string','float')
'String id immutable'
c.maketeans('aeiou','12345')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c.maketeans('aeiou','12345')
AttributeError: 'str' object has no attribute 'maketeans'. Did you mean: 'maketrans'?
c.marketrans('aeiou','12345')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    c.marketrans('aeiou','12345')
AttributeError: 'str' object has no attribute 'marketrans'. Did you mean: 'maketrans'?
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'Str3ng 3d 3mm5t1bl2'
c.replace('1','0')
'String id immutable'
c
'String id immutable'
'string,is,immutable'.split('-')
['string,is,immutable']
'string is immutable'.split(',')
['string is immutable']
a='''
python
progaramming
lang'''

s
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s
NameError: name 's' is not defined
s='''
python
programming
lang'''
s
'\npython\nprogramming\nlang'
>>> s.splitlines()
['', 'python', 'programming', 'lang']
>>> ['','python','programming','lang'].join()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    ['','python','programming','lang'].join()
AttributeError: 'list' object has no attribute 'join'
>>> ''.join(['', 'python', 'programming', 'lang'])
'pythonprogramminglang'
>>> ' '.join(['', 'python', 'programming', 'lang'])
' python programming lang'
>>> 'python.py.partition('.')
SyntaxError: unterminated string literal (detected at line 1)
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> s='java,python,c,c++'
>>> s.partition(',')
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
('java,python,c', ',', 'c++')
>>> c = '      hello      world          '
>>> 
>>> c
'      hello      world          '
>>> c.split()
['hello', 'world']
>>> c.lstrip()
'hello      world          '
>>> c.rstrip()
'      hello      world'
>>> text = "hello 🙂"
>>> tect.encode()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    tect.encode()
NameError: name 'tect' is not defined. Did you mean: 'text'?
>>> text.encode()
b'hello \xf0\x9f\x99\x82'
>>> b' hello \xf0\x9f\x99\x82'.decode()
' hello 🙂'
