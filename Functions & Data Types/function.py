Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
8
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
8
Traceback (most recent call last):
  File "D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py", line 8, in <module>
    mysum(3+6)
TypeError: mysum() missing 1 required positional argument: 'y'
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
8
9
22
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
24
11.0
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
5
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
Traceback (most recent call last):
  File "D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py", line 32, in <module>
    print(mysum2(3,5))
NameError: name 'mysum2' is not defined
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
8
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
8
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
0
5
0
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
0
0
0
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
0
5
5
>>> a='abd'
>>> b="abdo"
>>> c='''abdo'''
>>> a
'abd'
>>> b
'abdo'
>>> c
'abdo'
>>> x='what's your'
SyntaxError: invalid syntax
>>> x = "what's your"
>>> x
"what's your"
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py

abdo
    elsaeid
           abdo
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
my name is name and i am age years old
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
my name is abdo and i am 28 years old
>>> s = "my name is abdo and i am 28 years old"
>>> s
'my name is abdo and i am 28 years old'
>>> s+s
'my name is abdo and i am 28 years oldmy name is abdo and i am 28 years old'
>>> s*3
'my name is abdo and i am 28 years oldmy name is abdo and i am 28 years oldmy name is abdo and i am 28 years old'
>>> s.upper()
'MY NAME IS ABDO AND I AM 28 YEARS OLD'
>>> s.lower()
'my name is abdo and i am 28 years old'
>>> s.title()
'My Name Is Abdo And I Am 28 Years Old'
>>> s.isupper()
False
>>> s.islower()
True
>>> s.istitle()
False
>>> s.replace('i','we')
'my name wes abdo and we am 28 years old'
>>> s.split(' ')
['my', 'name', 'is', 'abdo', 'and', 'i', 'am', '28', 'years', 'old']
>>> path = "D:/Full Stack Django/Dev/01 Python_Basics/Functions"
>>> path.split('/')
['D:', 'Full Stack Django', 'Dev', '01 Python_Basics', 'Functions']
>>> path.split('/')[-1]
'Functions'
>>> s
'my name is abdo and i am 28 years old'
>>> s[0]
'm'
>>> s[4]
'a'
>>> s[-1]
'd'
>>> s[0:5]
'my na'
>>> s[:5]
'my na'
>>> s[5:]
'me is abdo and i am 28 years old'
>>> s[5::2]
'm sad n  m2 er l'
>>> t = [1,2,3,4,5,True,[1,2,3]]
>>> t[0]
1
>>> t[-1]
[1, 2, 3]
>>> t[0]=100
>>> t
[100, 2, 3, 4, 5, True, [1, 2, 3]]
>>> t.append(500)
>>> t
[100, 2, 3, 4, 5, True, [1, 2, 3], 500]
>>> t.insert(0,200)
>>> t
[200, 100, 2, 3, 4, 5, True, [1, 2, 3], 500]
>>> t.remove(200)
>>> t
[100, 2, 3, 4, 5, True, [1, 2, 3], 500]
>>> t.pop()
500
>>> t
[100, 2, 3, 4, 5, True, [1, 2, 3]]
>>> y = [1,2,3,4,34,20,200,500]
>>> y.sort()
>>> y
[1, 2, 3, 4, 20, 34, 200, 500]
>>> y.sort(reverse = True)
>>> y
[500, 200, 34, 20, 4, 3, 2, 1]
>>> y*2
[500, 200, 34, 20, 4, 3, 2, 1, 500, 200, 34, 20, 4, 3, 2, 1]
>>> k = (1,2,3,4,5,True)
>>> k[0]
1
>>> k[0]=100
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    k[0]=100
TypeError: 'tuple' object does not support item assignment
>>> q = list(k)
>>> 1
1
>>> q
[1, 2, 3, 4, 5, True]
>>> min(k)
1
>>> max(k)
5
>>> len(y)
8
>>> d = {'abdo':55,'ali':34}
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['abdo']
55
>>> d['hassan'] = 33
>>> d
{'abdo': 55, 'ali': 34, 'hassan': 33}
>>> d['hassan']=77
>>> d
{'abdo': 55, 'ali': 34, 'hassan': 77}
>>> d.values()
dict_values([55, 34, 77])
>>> d.keys()
dict_keys(['abdo', 'ali', 'hassan'])
>>> d.items()
dict_items([('abdo', 55), ('ali', 34), ('hassan', 77)])
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
abdo
ali
hassan
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
55
34
77
>>> 
= RESTART: D:/Full Stack Django/Dev/01 Python_Basics/Functions & Data Types/Functions & Data Types.py
abdo 55
ali 34
hassan 77
>>> 