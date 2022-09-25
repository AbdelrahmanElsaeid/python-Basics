
'''
for x in [1,2,3,4,5,6,7]:
    print(x)


range(10)
range(2,10)
range(2,10,2)
'''
'''
for x in range(5):

    for y in range(3):
        print(x,y)
'''
''''
for x in range(1,11):
    for y in range(1,13):
        print(f"{x} X {y} = {x*y}")
    print('---------')    
'''
'''
x = 0
while x<10 :
    print(x)
    x+=1
'''
'''
x = 0
while x<5 :
    y = 0
    while y < 10:
        print(x,y)
        y +=1
    
    x+=1
'''
'''
for x in range(10):
    if x ==5 :
        break
    print(x)
print('done')    
'''
'''
for x in range(10):
    if x ==5 :
        continue
    print(x)
print('done')    

'''

'''
start = int(input("Enter Start :"))
end = int(input("Enter End :"))


print(type(start))

print('Number\tSquare')
print('-----------------------')

for x in range(start,end):
    print(x,'\t',x*x)

'''

'''
row = int(input("Enter row :"))
col = int(input("Enter col :"))

for x in range(row):
    for y in range(col):
        print('*',end='')
    print(' ')    

'''

for x in range(8):
    for y in range(x+1):
        print('*',end = '')
    print(' ')    












