"""
Exercise 5
Please replace some bad words in the string to 'xxx' symbols
For example, for string "this is bad and bug words" with bad and bug bad words should be print this is xxx and xxx words*
You can use operator for
for currentWords in listWithBadWords :
operatotors here
You can use replace functions: str = str. replace( old, new )
"""
print("***************************************\n")
str = "this is bad and bug words"

bedword1 = "bug"
bedword2 = "bad"

#word_set = set(str.split())
word_list = str.split(" ")
print(word_list,type(word_list))
for i in range(len(word_list)):
    if (word_list[i] == bedword1) or (word_list[i] == bedword2):
        word_list[i] = "xxx"
    print(word_list[i])
print(word_list)

print("***************************************\n")
""" Exercise 7¶
Write Sorted function with parameters l as list and p as predicate function with two parameters
Predicate function compare first and second parameters and return true or false
Sorted function use predicate function for sorted list
For example, you program:
x = [2,3,4,1,5,6,7]
print(Sorter(x,lambda i,j: i > j))
should be print:
[7, 6, 5, 4, 3, 2, 1]"""