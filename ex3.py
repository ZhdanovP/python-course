'''
Create list l1, that contains elements: 'abcd', 786 , 2.23, 'john', 70.2
Print the complete list l1
Print the first element of the list
Print elements starting from 2nd with the 3rd element
Print Duplicate elements in list
'''

l1 = ['abcd', 786 , 2.23, 'john', 70.2]
print(l1)
print(l1[0])
print(l1[1:3])
print(l1*2) #one variant for duplicates
l1_duplicates = l1.copy()*2
print(l1_duplicates) #another variant for duplicates
# result l1 = ['abcd', 786, 2.23, 'john', 70.2]

'''
Create list l2, that contains elements: ‘second’, ’123’
Create list l3, that contains l1 and l2. Update l1[1] value. Verify l3 values.
Create list l4, that contains all elements of l2. Updated l2[0] value. Print l4.
'''

l1 = ['abcd', 786, 2.23, 'john', 70.2]
l2 = ['second', '123']
l3 = []
l3.append(l1)
l3.append(l2)
print(l3)
l1[1] = 999
print(l3)
l4 = l2.copy()
print(l4)
l2[0] = 555
print(l2)
print(l4)
# my result l1=['abcd', 999, 2.23, 'john', 70.2]
# my result l2=[555, '123']
# my result l3=[['abcd', 999, 2.23, 'john', 70.2], [555, '123']]
# my result l4=['second', '123']


'''
Create list l5 with 4 elements.
Using slice operator, update first 2 items to have values ‘1’ and ‘2’.
Insert list [7,7,7,7,7,7] after value ‘1’
Insert a copy of itself at the beginning.
Clear list
Create list l6 that has l1, l2, l5 elements as list. Update first element of list l1. Print l6
Sort and count the items of lists l1,l2,l3.
'''
l1 = ['abcd', 786 , 2.23, 'john', 70.2]
l5 = [1, 2, 3, 4]
print(l5)
l5[0:2] = [111, 222]
print(l5)
l5.insert(1, [7,7,7,7,7,7])
print(l5)
l5_copy = l5.copy()
l5.insert(0, l5_copy)
print(l5)
#l5.clear() commented as it ruins the further prints

l6 = []
l6.append(l1)
l6.append(l2)
l6.append(l5)

l1[0] = 9999
print(l6)

l1.sort() 
#can't sort l1-l3 because they containt different types of data

#my result l1=[9999, 786, 2.23, 'john', 70.2]
#my result l2=[555, '123']
#my result l3=[['abcd', 999, 2.23, 'john', 70.2], [555, '123']]
#my result l4=['second', '123']
#my result l5=[[111, [7, 7, 7, 7, 7, 7], 222, 3, 4], 111, [7, 7, 7, 7, 7, 7], 222, 3, 4]
#my result l6=[[9999, 786, 2.23, 'john', 70.2], [555, '123'], [[111, [7, 7, 7, 7, 7, 7], 222, 3, 4], 111, [7, 7, 7, 7, 7, 7], 222, 3, 4]]



'''
Create tuple t1 that contains elements: 'abcd', 786 , 2.23, 'john', 70.2
Update the first element of the tuple.
Return the number of elements that are forming a tuple.
Create tuple t2 based on l2 elements.
What is the minimum value of tuple t1? Can you sort tuple t1?
'''
t1 = ('abcd', 786 , 2.23, 'john', 70.2)
print(t1)
t1_list = list(t1)
t1_list[0] = 999
t1_tuple = tuple(t1_list)
print(t1_tuple)
print(len(t1))
t2 = tuple(l2)
print(t2)
#it is not possible to get min value and sort tuples they contain different types of data

#my result t1=('abcd', 786, 2.23, 'john', 70.2)
#my result t2=(555, '123')

'''
Create dictionary d1 that contains : 'one':'First',2:"Second",3:3
Print dictionary keys. Print dictionary values.
Can you sort a dictionary?
Verify that d1 has key ‘one’. Get value for key ‘one’. Get value for key ‘two’ (not 2 – look what will happen, and check type() of the value).
Create dictionary d2 using d1’s keys. Print d2.
Create dictionary d3 having l1, t1 and d2 as values.
'''
l1 = [9999, 999, 2.23, 'john', 70.2]
t1= (999, 786, 2.23, 'john', 70.2)
d1 = {'one':'First',2:"Second",3:3}
print(d1)
print(d1.keys())
print(d1.values())
#no dicts can't be sorted
if d1['one']:
    print(d1['one'])
#when try to print 'two' receive Traceback error "KeyError: 'two'" as this key does not exist
d2 = {}
d2_keys = d1.keys()
#print(d2_keys)
for d in d2_keys:
    d2.setdefault(d, 0)
print(d2)
d3 = {}
d3.update({
    'l1': l1,
    't1': t1,
    'd2': d2
})
print(d3)















