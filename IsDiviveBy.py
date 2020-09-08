def is_divide_by(number, a, b):
    if number % a == 0:
        if number % b == 0:
            return True
    return False

list = [[10, 2, 5], [7,1,3], [-12, 2, -5],
        [45, 5, 15],[15, -5, 3],[-831, 4, -7]]
result = [True, False, False, True, True, False]
i = 0
flag = True
for l in list:
    if is_divide_by(l[0],l[1],l[2]) != result[i]:
        print('Error in ', i, ' position')
        flag = False
    i = i + 1
if flag: print('Code is okey :)')

