import re

val = [1,4.5,8]
s = "2,3,4.7,5"
r = s.split(",")


for v in r:
    if type(v) == float:
        print(v, "es deciamal")
    else:
        print(v, "no es")