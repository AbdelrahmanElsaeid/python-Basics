#  List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


name = ["Ali", "Mahmoud" ,"sameh", "Abdelrahman", "Mahmoud", "Mohamed"]

newlist=[]

for x in name:
    if "o" in x:
        newlist.append(x)

print(newlist)        

#>>>>>>  ['Mahmoud', 'Mahmoud', 'Mohamed']

# list comprehension you can do all that with only one line of code:

#------------------------The Syntax---------------------------
#newlist = [expression for item in iterable if condition == True]


name2 = ["Ali", "Mahmoud" ,"sameh", "Abdelrahman", "Mahmoud", "Mohamed"]

newlist2 = [x for x in name if "o" in x]

print(newlist2)

#>>>>>>  ['Mahmoud', 'Mahmoud', 'Mohamed']
