#Exercise 7
#
#Write Sorted function with parameters l as list and p as predicate function with two parameters
#Predicate function compare first and second parameters and return true or false
#Sorted function use predicate function for sorted list
#For example, you program:

def swap(a, b):
    return b, a

def sort_buble(l, comparer):
    for i in range(len(l) - 1, -1, -1):
        for j in range(i):
            if comparer(l[j], l[j + 1]):
                l[j], l[j + 1] = swap(l[j], l[j + 1])

x = [2,3,4,1,5,6,7]
print(x)
sort_buble(x, lambda i, j: i < j)
print(x)
