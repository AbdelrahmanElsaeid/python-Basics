Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #● Create a Boolean variable named x

>>> x = True 

>>> print(type(x))

<class 'bool'>
>>> #● Create an integer variable named y
>>> y = 1000
>>> print(type(y))
<class 'int'>
>>> #● Create a float variable named z

>>> z = 8.7
>>> print(type(z))

<class 'float'>
>>> #● Create a string variable names s

>>> s = "My_Name"

>>> print(type(s))

<class 'str'>
>>> #● Convert the int variable to float

>>> x = 7

>>> print(type(x))

<class 'int'>
>>> x = 7.6

>>> print(type(x))

<class 'float'>
>>> # ● Can we convert the str to int ?   YES

>>> x = '50'

>>> print(type(x))

<class 'str'>
>>> c = int(x)
print(type(c))

SyntaxError: multiple statements found while compiling a single statement
>>> x = '50'
>>> print(type(x))

<class 'str'>
>>> c = int(x)

>>> print(type(c))

<class 'int'>
>>> #● Create a list of numbers from 1 to 5

>>> list = [1,2,3,4,5]

>>> #● Create a tuple from 10 to 15

>>> tuple = (10,11,12,13,14,15)

>>> #● Convert the list to tuple

>>> list = [1, 2, 3, 4]

>>> con_tuple = tuple(list)

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    con_tuple = tuple(list)
TypeError: 'tuple' object is not callable
>>> #● Create a dict of 3 values

>>> info = {'name':'abdelrahman', 'age':22 ,'address':'Mit Ghamr'}

>>> #● Can we use semi colon ; with python 

#	NO
>>> #● Python is interpreted or compiled ?

#	Python is an interpreted
>>> #● What is the differences between low level & high level

#Low level:-
#	it is hard to program   
#	it is easy to executed 
#	it consists of 1,0 
#	like C, Assembley 
#Hight level:-
#	take less time to be coded
#	easy to be correct
#	easy to program
#	like Java, Python ,C#
>>> #● What is the differences between = , ==

#	=  is Assignment operators which set variable in left and set value in right
>>> x = 10
c = 'name'
SyntaxError: multiple statements found while compiling a single statement
>>> #	== is comparison operator. use it when you compare between two value
>>> x=5
>>> x == 5
True
>>> x == 7
False
>>> #● What do we mean by using !=
	
#	check if the value of two operands is not equel if not return True

>>> #● What is the operator precedence
	
#	refer to the order of operations
>>> #● Create a variable x with value of 10
>>> x = 10

>>> #● Divide the x value by 5 using assignment operators

>>> x/=5

>>> x
2.0
>>> #● Increase x value by 15 using assignment operators

>>> x += 15

>>> x
17.0
>>> #● Multiply the x value by 10 using assignment operator

>>> x*=10

>>> x
170.0
>>> #● Get module of x on 3 using assignment operators

>>> x%=3

>>> x
2.0
>>> #● Using python print the module of 11 to 4

>>> print(11%4)

3
>>> #● Print the exponent of 2,3

>>> print(2**3)

8
>>> #● Divide 11 by 3 using python division

>>> print(11/3)

3.6666666666666665
>>> #● Can we divide 11 by 3 and get an integer number ?
#	YES
>>> 11//4
2
>>> #● Check if 10 is bigger than 15 or not
>>> if 10>15:
	print('yes')
else:
	print('no')

no
>>> #● If 10 is not bigger than15 print x is smaller than 15

>>> if 10<15:
	print('x is smaller than 15')
else:
	print('x is bigger than 15')

x is smaller than 15
>>> #● In which cases we will use all

#	The method returns True only if every element in iterable evaluates to True, and False otherwise 

#● What is the differences between all , and

#	The and operator return True only if all conditions are True

#● What is the differences between any , or
	
#	The method any return true if there are  element in iterable is true 

#● If we need all the conditions to be true we will use ….
	
#	 and
>>> #● What is the differences between if , elif
#  use elif when there are moare than one conditions

#● What is the differences between elif else

#  else ---> use it in the last statment condition there is no condition in here

#● Can we use more than one elif

#	yes

#● Can we use more than one else

#	 NO

#● write s simple ternary operator

#	print('true') if name = 'ALi' else print('false)

#● in elif , python will check all the conditions no matter what ?

#	yes

#● in elif we use else for ... ?

# if condition false
>>> #● if we have this list [2,4,6,8,10] :
#○ check to see if 4 in this list or not
>>> if 4 in list:
	print ('yes')
else:
	print('no')

yes
>>> #○ check to see if 4 and 6 in this list on not

>>> if 4 in list and 6 in list:
	print ('yes')
else:
	print('no')

no
>>> #○ check to see if 3 or 6 in this list

>>> if 3 in list or 6 in list:
	print ('yes')
else:
	print('no')

yes
>>> #○ check to see if 2 , 4 and 5 in this list

>>> if 2 in list and 4 in list:
	print ('yes')
elif 5 in list:
	print('yes 5')
else:
	print('no')

yes
>>> 