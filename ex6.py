def print2(text, **params):
    for i in params.items():
        if text.count(":" + str(i[0])):
            text = text.replace(":" + str(i[0]), str(i[1]))
    print(text)

printed_text = 'a = :result, b = :test'

print2(printed_text,test = 2,result = 'abcd')