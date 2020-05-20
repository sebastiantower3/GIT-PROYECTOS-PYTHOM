# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:58:29 2020

@author: Gato
"""


def isPrime(num):

#
# Su codigo Aqui   
#
     for i in range (2,num+1):
        if (num%i==0):
            if i==num:
               	return True 
            else:
                return False
                break

for i in range(1, 20):

                if isPrime(i + 1):

                   print(i + 1, end=" ")

