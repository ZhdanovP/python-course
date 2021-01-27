"""Part 1
Having a = 3, b =‘test’, c =[1,2,3] , d = ‘None’, e =None , f =0, what will be the values for the following operations:
a or b; a and b; a and c; a and d; b or d; a and e; a and f

Your program should be print:
3
test
[1, 2, 3]
test
None
0
"""
a = 3
b = 'test'
c = [1,2,3]
d = "None"
e = None
f = 0

print(a or b)
print(a and b)
print(a and c)
print(a and d)
print(b or d)
print(a and e)
print(a and f)

"""Part 2
Create a program that sets a value to a variable. It should print ‘Yes’ if the variable is number and the number is greater than 5. Prints ‘String’ if the variable is string. Prints ‘No’ if the variable is number and less than 5. Prints ‘other’ if the variable is nor string nor number. Don’t forget that floats are also numbers.
You not need use input, create variable directly! For type checking you can use type() function in if expression and compare with int, string or other types"""
print("*********************************************************")
print("Enter variable:")
var = input()
# var = "sting"
#?????????
if var.isdigit():
    var = int(var);

if (type(var) == int) and (var > 5):
	print("Yes")
elif type(var) == str:
	print("No")
else:
	print("Else")

"""Part 3
Having list l1 from “Data Structures”, print each element of the list on a line. Use for with range, enumerate and zip(x,y) functions. This function pack to tuple each element from x list and y list. For index you can use range() functions. First param - start index, second parameter - end index (not inclusive!)
Using while, print all the even values between 5 and 47.
Update program above to skip values 20, 24, 36.

Your program should be print:
(1, 'abcd') (2, 786) (3, 2.23) (4, 'john')
6 8 ... 44 46
6 8 ... 22 26 ... 34 38 40 42 44 46"""
print("*********************************************************")
l1 = ['abcd',786,2.23,'john']
l2 = [1,2,3,4]
print(l2)
print(list(zip(l2,l1)))
"""
i = 6
while i < 47:
    if a % 2 == 0:
        print(i," ")
   i += 1
"""

for i in range(6,46):
  if i % 2 == 0:
    print(i, end = ",")

