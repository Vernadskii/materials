'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in
a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that
fall out of that range must be rounded to the closest valid value.
rgb(255, 255, 255) returns FFFFFF
rgb(255, 255, 300)  returns FFFFFF
rgb(0,0,0)  returns 000000
rgb(148, 0, 211) returns 9400D3
'''

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
