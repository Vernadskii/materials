# На вход подается массив из возрастов
# Нужно вывести предпоследий и последний максимальный возраст

def two_oldest_ages(ages):
    ages.sort()
    result = [ages[-2+x] for x in range(2)]
    return result


l = [1, 5, 87, 45, 8, 8]
print(two_oldest_ages(l))

