# List Unpacking 


from functools import reduce
from re import X


x = 'abdelrahman'
y = 'elsaeid'

x + y

x = [1,2,3,4,5]
x = [1,2,3]
x,y,z = [1,2,3]

print(x)
print(y)
print(z)

t = [1,2,3,4,5,6,7,8,9,10]
head = t[0]
head
tail = t[1:]
tail



x,*y = [1,2,3,4,5,6,7,8,9]

print(x)

print(y)

*x,y = [1,2,3,4,5,6,7,8,9]

print(x)

print(y)



x,*_,y = [1,2,3,4,5,6,7,8,9]

print(x)

print(y)

for _ in range(5):
    print("Hello")

#---------------------------------

numbers = [1,2,3,4,5,6,7,8]
new_num = []
for n in numbers:
    new_num.append(n*n)
print(new_num)


new_num2 = [n*n for n in numbers]
print(new_num2)



new_num2 = [n*m for n in range(1,3) for m in range(1,5)]
print(new_num2)



even = [n for n in range(1,101) if n%2==0]
print(even)



#--------------------------------------------------------


numbers = [1,2,3,4,5,6,7,8,9]

def mysquare(n):
    return n*n


new_numbers = map(mysquare,numbers)
print(new_numbers)
print(type(new_numbers))
print(list(new_numbers))




number = list(range(1,100))
def even_filter(n):
    if n%2==0:
        return True

even = list(filter(even_filter,number))
print(even)


from functools import reduce
numbers = [1,2,3,4,5,6,7,8]

def mysum(x,y):
    return x+y


res = reduce(mysum,numbers)
print(res)


