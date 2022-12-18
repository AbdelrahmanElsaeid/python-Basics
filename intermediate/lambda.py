
#   A lambda function is a small anonymous function.

#   A lambda function can take any number of arguments, but can only have one expression.


#   syntax

#   lambda arguments : expression

a = lambda a,b: a+b

print(a(10,3))

#>>>>>>>>>>>>>>>  13

def myfun(n):
    return lambda a: a*n

s = myfun(4)
print(s(11))

#>>>>>>>>>>>>>>>  44
x = myfun(5)
print(x(11))

#>>>>>>>>>>>>>>>  55