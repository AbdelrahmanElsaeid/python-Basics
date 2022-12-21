# The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function.
#  It is used to pass a non-key worded, variable-length argument list. 



def sum(*args):
    res = 0
    for i in args:
        res +=i
    return res 

print(sum(1,2,3,4,5))       


#    **kwargs

def fun(**kwargs):
    for key,value in kwargs.item():
        print(f"{key} == {value}")
        
fun(first-name='Abdelrahman', mid-name='Elsaeid', last-name='Abdoelsoud')        
