print("""
#Part 1
#
#Having a = 3, b =‘test’, c =[1,2,3] , d = ‘None’, e =None , f =0, what will be the values for the following operations:
#a or b; a and b; a and c; a and d; b or d; a and e; a and f
#
#Your program should be print:
""")

a = 3
b ='test'
c =[1,2,3]
d = 'None'
e = None
f = 0

toPrint = ''
def evaluate(param):
    global toPrint
    if (param):
        toPrint = str(param)
    return param
        
print("\na or b:")
if evaluate(a) or evaluate(b):
    print(toPrint)

print("\na and b:")
if evaluate(a) and evaluate(b):
    print(toPrint)

print("\na and c:")
if evaluate(a) and evaluate(c):
    print(toPrint)

print("\na and d:")
if evaluate(a) and evaluate(d):
    print(toPrint)

print("\nb or d:")
if evaluate(b) or evaluate(d):
    print(toPrint)

print("\na and e:")
if evaluate(a) and evaluate(e):
    print(toPrint)

print("\na and f:")
if evaluate(a) and evaluate(f):
    print(toPrint)


print("""


#Part 2

#Create a program that sets a value to a variable. It should print ‘Yes’ if the variable is number and the number is greater than 5. Prints ‘String’ if the variable is string. Prints ‘No’ if the variable is number and less than 5. Prints ‘other’ if the variable is nor string nor number. Don’t forget that floats are also numbers.
#You not need use input, create variable directly! For type checking you can use type() function in if expression and compare with int, string or other types
""")

def is_float(s):
    try:
        i = float(s)
        return True;
    except ValueError:
        return False;

value = input()
if (is_float(value) and float(value) > 5):
    print("Yes")
elif (is_float(value)):
    print("No")
else:
    print("String")


print("""


#Part 3
#
#Having list l1 from “Data Structures”, print each element of the list on a line. Use for with range, enumerate and zip(x,y) functions. This function pack to tuple each element from x list and y list. For index you can use range() functions. First param - start index, second parameter - end index (not inclusive!)
#Using while, print all the even values between 5 and 47.
#Update program above to skip values 20, 24, 36.
""")

l1 = ['abcd', 786 , 2.23, 'john', 70.2 ]
for item in zip(range(1, len(l1)), l1):
    print(item, end = "")

print('\n')

i = 5;
while i <= 47:
    if not (i % 2):
        print(i, end = " ")
    i += 1;

print('\n')

i = 5;
exclude = [20, 24, 36]
while i <= 47:
    if (not (i % 2) and not exclude.count(i)):
        print(i, end = " ")
    i += 1;

