#!/usr/bin/python3

# read the lines from the file
fh = open('lines.txt')
for line in fh.readlines():
    print(line)         # the print() function inserts a new line character at the end
                        # can remove the new line by using print(line, end='')
