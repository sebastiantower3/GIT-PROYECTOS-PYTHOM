# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:10:27 2020

@author: Gato
"""

while True:
    x=input("Enter a number to count to: ")
    if x== 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
