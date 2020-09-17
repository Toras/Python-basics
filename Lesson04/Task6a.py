from itertools import count
from sys import argv


sc_name, t, max_t = argv
k = 1
for i in count(int(t)):
    print(i)
    k += 1
    if k > int(max_t):
        break
