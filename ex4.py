# Ex 4
# Part 1
a = 3; b = 'test'; c = [1, 2, 3]; d = 'None'; e = None; f = 0

def verify_pair(arg1, arg2, op):
    if op == "or":
        if arg1:
            return arg1
        else:
            return arg2
    elif op == "and":
        if not arg1:
            return arg1
        else:
            return arg2
    else:
        print("Incorrect third argument")


print("a or b")
print(verify_pair(a, b, "or"), "\n")

print("a and b")
print(verify_pair(a, b, "and"), "\n")

print("a and c")
print(verify_pair(a, c, "and"), "\n")

print("a and d")
print(verify_pair(a, d, "and"), "\n")

print("b or d")
print(verify_pair(b, d, "or"), "\n")

print("a and e")
print(verify_pair(a, e, "and"), "\n")

print("a and f")
print(verify_pair(a, f, "and"), "\n")

# Part 2
a = input()
res = ""

try:
    a = float(a)
    if a >5:
        res = "Yes"
    else:
        res = "No"

except ValueError:
    if type(a) is str:
        res = "String"
    else:
        res = "Other"

print(res)

# Part 3
"""
* Having list l1 from “Data Structures”, print each element of the list on a line. Use for with range,
enumerate and zip(x,y) functions. This function pack to tuple each element from x list and y list.
For index you can use range() functions. First param - start index, second parameter - end index (not inclusive!)
* Using while, print all the even values between 5 and 47.
* Update program above to skip values 20, 24, 36.
"""

l1 = ['abcd', 786 , 2.23, 'john', 70.2 ]
for i in zip(range(1, len(l1)), l1):
    print(i)
print()

i = 5
while i <= 47:
    if i % 2 == 0:
        print(i, end = " ")
    i += 1
print()

i = 5
while i <= 47:
    if i % 2 == 0 and i != 20 and i != 24 and i != 36:
        print(i, end = " ")
    i += 1