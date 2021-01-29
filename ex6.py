'''
Write you version print function with name print2. You can use only named parameters for this function. For start format parameter please use ":" delimeter.
For example: print2('a = :result, b = :test',test = 2,result = 'abcd') should be print 'a = abcd, b = 2
'''

def print2(ab, test, result):
    args = (ab, test, result)
    result_str = ''
    test = str(test)
    result = str(result)
    if ':' in ab:
        ab = ab.split(', ')
        for el in ab:
            whereColon = el.index(':') 
            result_var = el[:whereColon]     
            var_arg = el[whereColon+1:]     
            if var_arg == 'result':
                result_str = result_str + result_var + result + ', '
            elif var_arg == 'test':
                result_str = result_str + result_var + test
            else: print('nothing was found')
    return(result_str)

print2('a = :result, b = :test', 3433, 'sdfaserw') # 'a = sdfaserw, b = 3433'
