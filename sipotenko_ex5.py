#Please replace some bad words in the string to 'xxx' symbols
#For example, for string "this is bad and bug words" with bad and bug bad words should be print this is xxx and xxx words*
#You can use operator for
#for currentWords in listWithBadWords :
#operatotors here
#You can use replace functions: str = str. replace( old, new )

bad_words = ['bad', 'bug']
input_str = "this is bad and bug words"

print(input_str)

for word in bad_words:
    if input_str.find(word) != -1:
        input_str = input_str.replace(word, 'xxx')
        
print(input_str)
