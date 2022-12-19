# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

#----------------syntax---------------------
 #      map(fun, iter)



def mul(num):
    return num * num


numbers = (1, 2, 3, 4)
result = map(mul, numbers)
print(list(result)) 



#   We can also use lambda expressions with map to achieve above result.

result2 = map(lambda n: n*n,numbers)
print(list(result2))