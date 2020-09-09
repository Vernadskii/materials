#Найти степень числа в n ячейке массива в n-ой степени
def index(array, n):
    if n >= len(array):
        return -1
    else:
        return array[n]**n

def index1(array, n):
    try:
        return array[n]**n
    except:
        return -1