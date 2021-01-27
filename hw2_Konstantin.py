
print("***************************************\n")
l1 = ['abcd', 786 , 2.23, 'john', 70.2]
print(l1,"\n")
print(l1[0],"\n")
print([l1[1],l1[2]],"\n")
print(l1+l1,"\n")

print("***************************************\n")
l2 =['second','123'] 
l3 = l1,l2
print(l3,"\n") # Create list l2, that contains elements: ‘second’, ’123’
l1[1] = 999
print(l3,"\n") # Create list l3, that contains l1 and l2. Update l1[1] value. Verify l3 values.
l4 = list.copy(l2)
print(l4,"\n")
l2[0] = 555    # Updated l2[0] value
print(l2,"\n")
print(l4,"\n")

print("***************************************\n")
l5 = [1,2,3,4]
print(l5,"\n")
l5[0] = 111
l5[1] = 222 
print(l5,"\n")
l5.insert(1,[7,7,7,7,7,7])
l5.insert(0,list.copy(l5))
print(l5,"\n")  # [[111, [7, 7, 7, 7, 7, 7], 222, 3, 4], 111, [7, 7, 7, 7, 7, 7], 222, 3, 4]

l6 = [l1,l2,l5]
print(l6,"\n") # [['abcd', 786, 2.23, 'john', 70.2], [555, '123'], [[111, [7, 7, 7, 7, 7, 7], 222, 3, 4], 111, [7, 7, 7, 7, 7, 7], 222, 3, 4]]
l1[0] = 9999
print(l6,"\n")
#print(l1.sort(),"\n") #TypeError: '<' not supported between instances of 'str' and 'float'
print("***************************************\n")

""" Create tuple t1 that contains elements: 'abcd', 786 , 2.23, 'john', 70.2
Update the first element of the tuple.
Return the number of elements that are forming a tuple.
Create tuple t2 based on l2 elements.
What is the minimum value of tuple t1? Can you sort tuple t1?

Your program should be print:
('abcd', 786, 2.23, 'john', 70.2)
(999, 786, 2.23, 'john', 70.2)
5 (555, '123')

Please explain why your can't get min value of t1 and can't sort it
"""
t1 = tuple()
t1 = ('abcd', 786, 2.23, 'john', 70.2)
print(t1,"\n")
lst = list(t1)
lst[0] = '999'
t1 = tuple(lst)
print(t1,"\n")

print("***************************************\n")
"""Create dictionary d1 that contains : 'one':'First',2:"Second",3:3
Print dictionary keys. Print dictionary values.
Can you sort a dictionary?
Verify that d1 has key ‘one’. Get value for key ‘one’. Get value for key ‘two’ (not 2 – look what will happen, and check type() of the value).
Create dictionary d2 using d1’s keys. Print d2.
Create dictionary d3 having l1, t1 and d2 as values.

Your program should be print:
{'one': 'First', 2: 'Second', 3: 3}
True
{'one': 0, 2: 0, 3: 0}
{'l1': [9999, 999, 2.23, 'john', 70.2], 't1': (999, 786, 2.23, 'john', 70.2), 'd2': {'one': 0, 2: 0, 3: 0}}"""

d1 = dict()
d1['one'] = 'First'
d1[2] = "Second"
d1[3] = 3
print(d1)
print(d1.keys())
print(d1.values())
