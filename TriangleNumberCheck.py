'''
A triangle number is a number where n objects form an equilateral triangle
(it's a bit hard to explain). For example, 6 is a triangle number because you
can arrange 6 objects into an equilateral triangle:
  1
 2 3
4 5 6

8 is not a triangle number because 8 objects do not form an equilateral triangle:
   1
  2 3
 4 5 6
7 8
In other words, the nth triangle number is equal to the sum of the n natural numbers from 1 to n.
'''


def is_triangle_number(number):
    if number == 0: return True
    count_help = 2
    interm_res = 1
    if isinstance(number, int):
        while interm_res < number:
            interm_res += count_help
            count_help += 1
            #print(interm_res)
        if interm_res == number:
            return True
        else:
            return False
    else:
        return False

print(is_triangle_number(0))