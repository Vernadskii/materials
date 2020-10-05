'''
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
returns 'Bart, Lisa & Maggie'
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
returns 'Bart & Lisa'
namelist([ {'name': 'Bart'} ])
returns 'Bart'
namelist([])
returns ''
'''

def namelist(names):
    res = ''
    length = len(names)
    for i in range(length):
        print(i)
        if (i == length-1)and(length != 1):
            res += '& '
            res += " ".join(list(names[i].values()))
        else:
            if length == 1:
                res += " ".join(list(names[i].values()))
            else:
                if i == length - 2:
                    res += " ".join(list(names[i].values()))
                    res += ' '
                else:
                    res += " ".join(list(names[i].values()))
                    res += ', '
    return res



print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist([ {'name': 'Bart'} ]))