text = "this is bad and bug words"
listWithBadWords = ["bad", "bug"]

new_text = text
for currentWord in listWithBadWords:
    new_text = new_text.replace(currentWord, "xxx")

print(text)
print(new_text)