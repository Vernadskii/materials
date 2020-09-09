# Преобразовать строку в новую строку, где каждый символ в новой строке равен "(",
# если этот символ появляется только один раз в исходной строке, или ")",
# если этот символ встречается более одного раза в исходной строке строка.
# Игнорировать использование заглавных букв при определении одной буквы.

def duplicate_encode(word):
    #your code here
    word = word.lower()
    print(word)
    result = ''
    for s in word:
        if word.count(s) > 1:
            result += ')'
        else:
            result += '('
    return result

print(duplicate_encode("Success"))