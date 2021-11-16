# https://book.pythontips.com/en/latest/map_filter.html
# https://pythonacademy.com.br/blog/a-biblioteca-itertools-do-python

import os
from itertools import permutations, product, count

x = 2
y = 2
z = 2
n = 2

# core logic
def fn1():
    for i in range(0, x + 1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                if (i + j + k) != n:
                    print([i, j, k])
               
# itertools
def fn2():
    l = list(permutations( [x, y, z], 3))
    print(l)


# Hacker rank solution
def fn3():
    list1 = list(permutations( [x, y, z], 3))
    #list1 = list(filter(lambda l, n=n: l[0]+l[1]+l[2] != n, list1))
    print(str(list1).replace("(", "[").replace(")","]"))


os.system("cls")        
print(list(permutations( [0,3,1], 3)))
