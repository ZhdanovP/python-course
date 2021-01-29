print("""
#========> Part 1

#Create list l1, that contains elements: 'abcd', 786 , 2.23, 'john', 70.2
#Print the complete list l1
#Print the first element of the list
#Print elements starting from 2nd with the 3rd element
#Print Duplicate elements in list
#
#You program should be print:
#
#   ['abcd', 786, 2.23, 'john', 70.2]
#
#    abcd
#
#    [786, 2.23]
#
#    ['abcd', 786, 2.23, 'john', 70.2, 'abcd', 786, 2.23, 'john', 70.2]
""")

l1 = ['abcd', 786 , 2.23, 'john', 70.2 ]
print(l1)
print(l1[0])
print(l1[1:3])

l1_double = l1.copy()
l1_double.extend(l1)
print(l1_double)


print("""



#========> Part 2

#Create list l2, that contains elements: ‘second’, ’123’
#Create list l3, that contains l1 and l2. Update l1[1] value. Verify l3 values.
#Create list l4, that contains all elements of l2. Updated l2[0] value. Print l4.
#
#Your program should be print:
#
#    [['abcd', 786, 2.23, 'john', 70.2], ['second', '123']]
#
#    [['abcd', 999, 2.23, 'john', 70.2], ['second', '123']]
#
#    ['second', '123']
#
#    [555, '123']
#
#    ['second', '123']
""")

l2 = ['second', '123']
l3 = [l1, l2]
print(l3)

l1[1] = 999
print(l3)

l4 = l2.copy()
print(l4)
l2[0] = 555
print(l2)
print(l4)


print("""



#========> Part 3

#Create list l5 with 4 elements.
#Using slice operator, update first 2 items to have values ‘1’ and ‘2’.
#Insert list [7,7,7,7,7,7] after value ‘1’
#Insert a copy of itself at the beginning.
#Clear list
#Create list l6 that has l1, l2, l5 elements as list. Update first element of list l1. Print l6
#Sort and count the items of lists l1,l2,l3.
#
#Your program should be print
#
#    [1, 2, 3, 4]
#
#    [111, 222, 3, 4]
#
#    [111, [7, 7, 7, 7, 7, 7], 222, 3, 4]
#
#    [[111, [7, 7, 7, 7, 7, 7], 222, 3, 4], 111, [7, 7, 7, 7, 7, 7], 222, 3, 4]
#
#    [['abcd', 786, 2.23, 'john', 70.2], [555, '123'], [[111, [7, 7, 7, 7, 7, 7], 222, 3, 4], 111, [7, 7, 7, 7, 7, 7], 222, 3, 4]]
#
#    [[9999, 786, 2.23, 'john', 70.2], [555, '123'], [[111, [7, 7, 7, 7, 7, 7], 222, 3, 4], 111, [7, 7, 7, 7, 7, 7], 222, 3, 4]]
""")

l5 = [1, 2, 3, 4]
print(l5)
l5[0:2] = 111, 222
print(l5)
l5.insert(1, [7,7,7,7,7,7])
print(l5)
l5.insert(0, l5.copy())
print(l5)

l6 = [l1, l2, l5]
print(l6)
l1[0] = 9999
print(l6)

# l1.sort()
# l2.sort()
l3.sort()
print("l1 count: ", len(l1))
print("l2 count: ", len(l2))
print("l3 count: ", len(l3))


print("""



#========> Part 4
#
#Create tuple t1 that contains elements: 'abcd', 786 , 2.23, 'john', 70.2
#Update the first element of the tuple.
#Return the number of elements that are forming a tuple.
#Create tuple t2 based on l2 elements.
#What is the minimum value of tuple t1? Can you sort tuple t1?
#
#Your program should be print:
#
#    ('abcd', 786, 2.23, 'john', 70.2)
#
#    (999, 786, 2.23, 'john', 70.2)
#
#    5 (555, '123')
#
#    Please explain why your can't get min value of t1 and can't sort it
""")

t1 = ('abcd', 786 , 2.23, 'john', 70.2)
print(t1)
print("""
# Update the first element of the tuple. => can not be updated due to read-only access
""")
print(len(t1))
t2 = tuple(l2)
print(t2)


print("""



#========> Part 5

#Create dictionary d1 that contains : 'one':'First',2:"Second",3:3
#Print dictionary keys. Print dictionary values.
#Can you sort a dictionary?
#Verify that d1 has key ‘one’. Get value for key ‘one’. Get value for key ‘two’ (not 2 – look what will happen, and check type() of the value).
#Create dictionary d2 using d1’s keys. Print d2.
#Create dictionary d3 having l1, t1 and d2 as values.
#
#Your program should be print:
#
#    {'one': 'First', 2: 'Second', 3: 3}
#
#    True
#
#    {'one': 0, 2: 0, 3: 0}
#
#    {'l1': [9999, 999, 2.23, 'john', 70.2], 't1': (999, 786, 2.23, 'john', 70.2), 'd2': {'one': 0, 2: 0, 3: 0}}
""")

d1 = {'one': 'First', 2: 'Second', 3: 3}
print(d1)
print(d1.keys())
print(d1.values())
print("""
# Can you sort a dictionary?
# Not exactly. There isn't standard way. However, if keys are of the same type, it is possible
# to implement kind of sorting algorithm
""")
print(d1.get('one') != None)
print(d1.get('one'))
print(d1.get('two'))

d2 = dict.fromkeys(d1, 0)
print(d2)

d3 = {'l1': l1, 't1': t1, 'd2': d2}
print(d3)

