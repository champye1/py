'''
costo=float(input("ingrese costo = "))

if costo<50000: 
     costo1=costo*costo*0.2
     print("costo resultante =",costo1)
else:
     costo2=costo-costo*0.4
     print("costo resultante = ",costo2)

'''

'''
precio=float(input("ingresar precio"))
if precio<10000: print("es mayor que 10000")
else:print("es menos que 10000")
'''

'''

#metodo optativo escribir todo sobre una linea y asi gastar menos lineas 
costo=float(input("ingrese costo = "))
if costo<50000: costo1=costo+costo*0.2;print("costo resultante =",costo1)
else: costo2=costo-costo*0.4; print("costo resultante = ",costo2)
'''

'''

#if ternario es un if que no es de paython que no solo es de este si no que se ocupa en todos los lenguajes de programacion

# codigo "si es que se cumple" if [condicion] else [codigo si no se cumple]

#en este caso todo va guardado dentro del codigo ocupando el if ternario donde la funcion es "print seguido de un if y terminando con un else"
num=int(input("ingresa numero entero ="))
print("es par " if num%2==0 else "es inpar")
'''

'''
#ejemplo dos de if ternario

nume=float(input("ingresar numerador de las division = "))
deno=float(input("ingresar denominador de la division = "))

div=nume/deno if deno and nume!=0 else "error, division por cero "
print(div)
print("fin")
#aqui ocupamos el if ternario donde se crea una variable div despues se pregunta si div es igual o distinto a 0 y en el else se muestra que el error

'''

'''
#ingresar la edad ed una persona si la persona es mayor de edad imprimir "mayor de edad si no menor de edad
edad=int(input("ingresar edad"))
print("mayor de edad " if edad>=18 else "menor de edad")
'''

'''
mensaje="mayor de edad" if edad<=18 else ("menor de edad")
print(mensaje)
'''

'''
#se pedira un sueldo , si el sueldo es mayor a 800000, se imprime mas un 5% y si es menor se imprime con un aumento de 10%

sueldo=float(input(" ingresa tu sueldo = "))
sueldoT=sueldo*0.05 if sueldo>800000 else sueldo*0.1
print(sueldoT)
'''

'''
#otra manera de hacer este mismo ejercicio

sueldo=int(input("ingresar sueldo))
print(0.05*sueldo if sueldo>800000 else 0.1*sueldo)
'''

'''
#para que sirve FOR  es una estructura ciclica ,reptitiva , iterativa o loop
#permite ejecutar una cantidad definida de veces 
#la sintaxis es 

for<element> in <itereable>:
     intrucciones
else:
     intrucciones

'''

'''
#EJEMPLO FOR
#range es una estructura iterable es una estructura que se puede recorrer 
for i in range(6):#range(6) entrega 0,1,2,3,4,5
    print("i= ", i ,end= " <-------> ")
    #en caso de que se pida que se muestre hacia la derecha  se ocupa el end= para que todo salga dentro de una misma linea 
else:#el else no se ejecutara cuando cuando haya un breack
    print("\n -fin- \n ")
    #la palabra fin la muestra despues de terminar de recorrer el range    #/n es una secuencia de escape para saltar de linea
'''

'''
#hay una intruccion que permite saltar un ciblo de for o del while, en caso de querer omitir alguna instruccion llamada CONTINUE

for i in range(6):
    if i%2==0:
        continue
    else:
        print("i = ",i)
else:
    print("\nfin\n")

'''

'''
#lectura de 4 costos

for i in range(1,5):
    Costo=float(input("ingrese costo "+str(i)+ "="))
    print(Costo)
'''
#otra manera de pedir estos 4 costos
'''
for i in range(1,5):
    print("ingrese costo",i,end="= ")
    costo=float(input())

'''

'''
cant=int(input("cantidad de notas = "))
if cant<4:
    for i in range(cant):
       nota=float(input("ingrese nota = "+str(i+1)+" = "))
       promedio=cant/nota
       print(promedio)
else:
    print("error")
    '''

'''
total=0
cant=int(input("ingresa cantidad de notas ="))
for i in range (cant):
    nota=float(input("ingrese nota"+str(i+1)+"="))
    total=total+nota
if cant>0:
    print("promedio =",round(total/cant,1))

from winsound import Beep
freq=1000
dura=800

Beep(freq,dura)
Beep(freq+200,dura+50)
Beep(freq+150,dura-20)
'''

'''
#el for puede usar un range que tiene un paso distinto a 1 

#Sintaxis:
#range(minimo,maximo,paso)
#ejemplo
#parte desde el numero 2 pero termina en el numero 21 
for num in range (2,22,2):
    print(num) #imprime desde los numeros pares desde el 2 al 20 aunque este termine en 21 
'''

'''
#EJEMPLO DE BREACK  QUE SE USA EN EN LOS BOOLEANA (PARA TRUE O FALSE ) PARA TERMINAR FORZADAMENTE EL FOR O WHILE

varbool=False #varbool es una variable booleana (cumple la funcion false o true)
#inicializamos en un valor falso (siempre el falso tendra valor 0 y el verdadero tendra valor 1 matematicamente )

correo=input("ingrese su e-mail= ")
for lector in correo: #el codigo lector recorre el texto de correo
    if lector=="@":
        varbool=True
        break
else:
    print('esto no deberia imprimirse si el correo esta weno')
if varbool==True:
    print("su correo esta weno")
else:
    print("correo ta malo")
'''
total=0
funcionario=int(input(" ingrese cantidad de funcionario = "))
for i in range (funcionario):
    sueldo=int(input("ingresa su sueldo base = "))
    total=total+sueldo
    promedio=total/funcionario
if promedio>1000000:
    print("sueldo alto")
else:
    print("bajo sueldo")
