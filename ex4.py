'''
Having a = 3, b =‘test’, c =[1,2,3] , d = ‘None’, e =None , f =0, what will be the values for the following operations:
a or b; a and b; a and c; a and d; b or d; a and e; a and f
'''

a = 3
b ='test'
c = [1,2,3]
d = 'None' 
e = None
f = 0

if a or b:
    if a: print(a)
    else: print(b)
    
if a and b:
    print(b)
else: print('No "a and b" found.')
    
if a and c:
    print(c)
else: print('No "a and c" found.')
    
if a and d:
    print(a)
else: print('No "a and d" found.')
    
if b or d:
    print(b)
else: print('No "b or d" found.')
    
if a and e:
    print(a)
else: print('None')
    
if a and f:
    print(0)
else: print('0')

'''
Part 2
Create a program that sets a value to a variable. It should print ‘Yes’ if the variable is number and the number is greater than 5. Prints ‘String’ if the variable is string. Prints ‘No’ if the variable is number and less than 5. Prints ‘other’ if the variable is nor string nor number. Don’t forget that floats are also numbers.
You not need use input, create variable directly! For type checking you can use type() function in if expression and compare with int, string or other types
'''

v = 11 # 3 5 6 'asd' 3.5 99.9 1j

if type(v) == str:
    print(v)
    
elif type(v) == int:
    if v > 5:
        print("Yes from int")
    else: print("No from int")
elif type(v) ==  float:
    v = round(v)
    if v > 5: print('Yes from float')
    else: print('No from float')
elif type(v) == complex:
    v = v.real
    if v > 5: print('Yes from complex')
    else: print('No from complex')
else: print('other')



'''
Part 3
Having list l1 from “Data Structures”, print each element of the list on a line. Use for with range, enumerate and zip(x,y) functions. This function pack to tuple each element from x list and y list. For index you can use range() functions. First param - start index, second parameter - end index (not inclusive!)
Using while, print all the even values between 5 and 47.
Update program above to skip values 20, 24, 36.
'''
l1 = ['abcd', 786, 2.23, 'john']
l1_str = ''
indexes_list = []
for index, el in enumerate(l1, start=1):
    l1_str = l1_str + str(el) + ', '
    indexes_list.append(index) 
l1_str = l1_str.split(', ')
zipped = zip(indexes_list, l1_str)
zipped = list(zipped)
for el in zipped:
    print(el, end=' ')
    
print('\n')

i = 5
while i < 47:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1


print('\n')

i = 5
while i < 47:
    if i == 20:
        i += 1
        continue
    elif i == 24:
        i += 1
        continue
    elif i == 36:
        i += 1
        continue
    
    if i % 2 == 0:
        print(i, end=' ')
    i += 1
else: i += 1