#leer dos pesos de  encomienda (en kilos)
#usan contro de excepciones valueerror para estas estructuras 
#calcular el 40% del primer valor
#calular el 60% del segundo valor
#sumar ambos calculos
#si el total es mayor a 50 escrbir "excedes limite " aqui va la diferencia entre 50 y el total en caso de lo contrario escribir dentro del limite"


totalvalor=0
try:
    valor1 = int(input('Ingrese el valor 1 ingresar='))
    while valor1<=0:
        valor1=int(input('Ingrese la valor mayor a 0 ='))
        valor1*=0.4
except ValueError:
    print("error de numero")



try:
    valor2=int(input('Ingrese la valor 2 mayor a 0 ='))
    while valor2<=0:
        valor2=int(input("error ingresa valor mayor a 0"))
        valor1*=0.6
except:
    print("error de numero")

totalvalor=valor1+valor2

print("su peso es  = ",round(totalvalor,2))


if totalvalor>50:
    print("execede el limite ",totalvalor)
else:
    print("esta en el limite ")