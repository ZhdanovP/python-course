'''
Please replace some bad words in the string to 'xxx' symbols
For example, for string "this is bad and bug words" with bad and bug bad words should be print this is xxx and xxx words*
'''

user_input = input() # e.g. this is bad and bug words
cleaned_user_input = user_input.split(' ')

final_string = ''
final_string2 = ''
for currentWord in cleaned_user_input:
    if currentWord == 'bad':
        currentWord = currentWord.replace('bad', 'xxx')
    elif currentWord == 'bug':
        currentWord = currentWord.replace('bug', 'xxx')
    else: pass
    final_string = final_string + currentWord + ' '
print(final_string)