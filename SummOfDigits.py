def digital_root(a):
    result = 0
    while a!= 0 :
        result = result + (a % 10)
        a = a // 10
    return result

a = int(input("Введите число: "))
print(digital_root(a), ' <-- result')