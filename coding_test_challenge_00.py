from email.headerregistry import Address
from multiprocessing.sharedctypes import Value
from tkinter import Variable


def print_array_items(n):
    myArr = []
    while n>0:
        myArr.insert(0,n)
        n -= 1
    print(*myArr, sep = ", ")
print_array_items(int(input()))

* - pointer Variable


Reference by Value
    int var: 
    a = 6
    b = a # b = 6
    a = 7 # a = 7
    print(b) # 6


Reference by Address