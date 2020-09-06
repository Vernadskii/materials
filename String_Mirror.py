def spin_words(sentence):
    sentence = sentence.split()
    result = ''
    count = len(sentence)
    for s in sentence:
        if count != 1:
            if len(s) >= 5:
                result = result + s[::-1] + ' '
            else:
                result = result + s + ' '
        else:
            if len(s) >= 5:
                result = result + s[::-1]
            else:
                result = result + s
        count = count - 1


    return result

#str = input("Введи строчку ")
str = 'Hello world my name Danya'
print(spin_words(str))
