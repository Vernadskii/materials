def rgb(r, g, b):
    l = [r,g,b]
    for i in range(3):
        if l[i] > 255:
            l[i] = 255
        elif l[i] < 0:
            l[i] = 0
    result = ''
    for i in l:
        if i // 10 == 0:
            hex_i_str = '0' + str(i)
            result += hex_i_str
        else:
            hex_i_str = str(hex(i))
            result += hex_i_str[2:]
        print(result)
    return result.upper()


print(rgb(8,255,255))
