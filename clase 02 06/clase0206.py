"""
from random import *

cant=int(input('Cantidad de personas='))
for i in range(cant):
    edad=randint(1,110)
    print('Edad '+str(i+1)+'=',edad)
"""




from random import *

cant=int(input("cantidad de contenedores sobrecargados "))
print("/t contenedores /t peso total(kg)")
for i in range(cant):
    peso=uniform(2300,32000)
    print('\t\t'+str(i+1)+'\t',round(peso,2))