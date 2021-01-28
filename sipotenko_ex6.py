# Exercise 6
#
# Write you version print function with name print2. You can use only named parameters for this function. For start format parameter please use ":" delimeter.
# For example: print2('a = :result, b = :test',test = 2,result = 'abcd') should be print 'a = abcd, b = 2

def print2(out, **args):
    for i, j in args.items():
        index = out.find(i)
        if (index and index != -1 and out[index - 1] == ':'):
            out = out.replace(':' + i, str(j))
            
    print(out)

print2('a = :result, b = :test',test = 2,result = 'abcd')
