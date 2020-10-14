"""
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-789
"""

def create_phone_number(n):
    res = "("
    res += ''.join(str(i) for i in n[:3])
    res += ") "
    res += ''.join(str(i) for i in n[3:6])
    res += "-"
    res += ''.join(str(i) for i in n[6:10])
    return res

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))