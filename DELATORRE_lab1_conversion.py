# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:10:34 2020

@author: Gato
"""
def l100kmtompg(liters):
    
    return ((100)*(1000)*(1/1609.344)*(3.79)*(1/liters))



def mpgtol100km(miles):
    
    return (((1/1000)*(1609.344)*(1/3.79)*(miles))**(-1))*100
         
print(l100kmtompg(3.9))

print(l100kmtompg(7.5))

print(l100kmtompg(10.))

print(mpgtol100km(60.3))

print(mpgtol100km(31.4))

print(mpgtol100km(23.5))