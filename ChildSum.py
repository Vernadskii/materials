def add(num1, num2):
    snum1 = str(num1)
    snum2 = str(num2)
    difference = len(snum1) - len(snum2)
    if difference >= 0:
        for i in range(abs(difference)):
            snum2 = '0' +snum2
    else:
        for i in range(abs(difference)):
            snum1 = '0' + snum1

    print(snum1)
    print(snum2)
    border = len(snum1)
    list = []
    for i in range(border):
        a = snum1[-i-1]
        #print(a)
        b = snum2[-i-1]
        #print(b)
        list.append(int(a)+int(b))
        #print(list)
    list.reverse()
    stroka = "".join(str(x) for x in list)
    print(stroka)


add(2014, 19)


