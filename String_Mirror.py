def spin_words(sentence):
    sentence = sentence.split()
    result = ''
    for s in sentence:
        if len(s) >= 5:
            result = result + s[::-1] + ' '
        else:
            result = result + s + ' '
    result = result.rstrip()
    return result

#str = input("Введи строчку ")
str = 'Hello world my name Danya'
print(spin_words(str))