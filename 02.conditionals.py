#!/usr/bin/python3

a, b = 0, 1
if a < b:
    print('a ({}) is less than b ({})'.format(a, b)) # The {} is replaced by the string in .format()
else:
    print('a ({}) is not less than b ({})'.format(a, b))

print("foo" if a < b else "bar");