'''
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
'''

def find_it(seq):
    a = set()
    for i in seq:
        if i in a:
            a.remove(i)
        else:
            a.add(i)
        res = "".join(str(e) for e in list(a))
    return int(res)


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))