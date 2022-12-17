# exception handling 


try:
    age = int(input("Enter age: "))
    print(100/age)
except ValueError as e:
    print("Enter number")
    print(e)    


except ZeroDivisionError :
    print("Enter number >0")

except Exception:
    print('error')    
        

#-----------------------------------------------------------

try:
    age = int(input("Enter age: "))
    print(100/age)
except Exception:
    print('error') 
else:
    print('no exceptions')

finally:
    print('always')

    
                     
