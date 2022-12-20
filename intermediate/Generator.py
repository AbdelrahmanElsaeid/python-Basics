#  Python Generators are the functions that return the traversal object and used to create iterators.

#  It is similar to the normal function defined by the def keyword and uses a yield keyword instead of return

def gen():
    for i in range(10):
        yield i

for a in gen():
    print(a)

#  The yield statement is responsible for controlling the flow of the generator function.
#  It pauses the function execution by saving all states and yielded to the caller.

# use multi yield

def mult_yield():
    n1 = "adam"
    yield n1
    n2 = "Mohamed"
    yield n2
    n3 = "Abdo"
    yield n3

my_obj = mult_yield()
print(next(my_obj))
print(next(my_obj)) 
print(next(my_obj))   


list = [1,2,3,4,5,6,7,8]
a = [i**3 for i in list]
print((a))
# >>>>>>>>>>  [1, 8, 27, 64, 125, 216, 343, 512]

list = [1,2,3,4,5,6,7,8]
a = [i**3 for i in list]
print(next(a))

# >>>>>>> TypeError: 'list' object is not an iterator   ERORR


list = [1,2,3,4,5,6,7,8]
a = (i**3 for i in list)
print(next(a))    #>>>>>>>  1
print(next(a))    #>>>>>>>  8
print(next(a))    #>>>>>>>  27
print(next(a))    #>>>>>>>  64