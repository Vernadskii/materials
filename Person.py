"""
Here is how the final refactored code would be used:

joe = Person('Joe')
joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
joe.name          # should == 'Joe'
"""
class Person:
    def __init__(self, name1):
        self.name = name1
    def greet(self, your_name):
        return "Hello %s, my name is %s" % (your_name, self.name)

jack = Person("Jack")
jill = Person("Jill")
print(jack.greet("Jill"))
print(jack.greet("Mary"))
print(jill.greet("Jack"))
print(jill.name)