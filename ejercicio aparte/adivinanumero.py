from random import *

intento=0

aleatorio=randint(1,10)

while True:
    numero=int(input(" ingrese un numero entero entre 1 al 10 ="))
    while numero<1 or numero>10:
        numero=int(input("error, ingresa un numero entero entre 1 al 10 ="))
    intento+=1
    if numero==aleatorio:
        print("correcto")
        break
print("cantidad de intentos = ",intento)
