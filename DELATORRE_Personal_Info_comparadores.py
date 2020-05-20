# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:05:00 2020

@author: Gato
"""

print("Bienvenido, para continuar llene la información solicitada: ")
FirstName= input("Ingrese su nombre: ")
LastName= input("Ingrese su Apellido: ")
Location= input("Ingrese su dirección: ")
Age= input("Ingrese su edad: ")


if Age >= 0 and Age <=15:
    print("Usted es muy Joven")
    
elif Age >= 16 and Age <I=40:
    print("Usted es Joven")
    
else:
    print("Usted es Adulto")

print("Verifique si la información ingresada es correcta")
print("Su nombre es "+FirstName+" "+LastName+" "+"vive en "+Location+" "+"y tiene "+Age+ " años" )