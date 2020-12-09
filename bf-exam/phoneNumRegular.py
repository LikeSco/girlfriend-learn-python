#!/usr/bin/python3

import re

txtfile = open("phoneNumber.txt", "r")
txtLines = txtfile.readlines()
pattern = re.compile('^(\d{3}-|\(\d{3}\)\s)\d{3}-\d{4}$')
result = ""
print(txtLines)

for line in txtLines:
    line = line.strip("\n")
    pNum = re.match(pattern, line.strip())
    if pNum:
        print(line)
        result += line + "\n"

with open("result.txt", "w") as f:
    f.write(result)
    f.close()
