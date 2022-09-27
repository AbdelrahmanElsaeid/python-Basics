'''
● In which cases we will use all
   
    if all elements in iterable are True return True otherwise return False



● What is the differences between all , and

    ----The all built-in function It is similar to the and operator
     returns True if all the elements of the iterable evaluate to True.

     ex:
     print(all([True, True, True]))
    >>> True

    print(all([True, True, False]))
    >>> False


    ----The "and" operator returns True if all the conditions are True. 
    ex:
    print((5==5) and ("abdo" == "abdo"))
    >>> True

    print((5==5) and ("abdo" == "elseaid"))
    >>> False


● What is the differences between any , or

    ----The any built-in function It is similar to the or operator 
    returns True if any of the elements of the iterable evaluate to True.
    ex:
    print(any([True, True, True]))
    >>> True

    print(any([True, True, False]))
    >>> True


    ----The or operator returns True if any of the conditions are True.

    ex:
       print((5==5) and ("abdo" == "abdo"))
        >>> True

        print((5==5) and ("abdo" == "elseaid"))
        >>> True



● If we need all the conditions to be true we will use

    ----  AND



● What is the differences between if , elif

    ----If there are only two options, you use      IF 

    ----If there are more options, you use          elif


● What is the differences between elif else

    ----Else is used  with if to define the alternative path if the condition
    in the if statement is incorrect.
    ----elif is used when there are more alternative path and contain condition. 




● Can we use more than one elif

    ---- YES



● Can we use more than one else

    ---- NO   


● write a program that take 2 numbers from the user and print
the numbers between them
'''

n1 = int(input("Enter number1 : "))
n2 = int(input("Enter number2 : "))

for x in range(n1 + 1,n2):
    print(x)


'''
● write a program that takes a number from the user and
prints the number from 0 to 100 that can be divided by this
number

'''

n = int(input("Enter number : "))

for x in range(101):
  if x % n == 0:
    print(x)
