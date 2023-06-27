'''Mientras responda s para seguir: 
Se lee el precio de un artículo (validar entre 10000 y 300000).
Al precio agregarle el IVA
Si el precio resultante es mayor a 200000
- restarle 10000,
- mostrar el precio0 final resultante y
- escribir el mensaje “Precio Alto”,
en caso contrario,
- restarle 5000,
- mostrar el precio final resultante y
- escribir “Precio Normal”'''
preciofinal=0
seguir="s"


while seguir=="s":
    precio=int(input("ingresar precio valido entre 10.000 y 30.000 = "))
    while precio<10000 or precio>30000:
         precio=int(input("ingresar precio valido entre 10.000 y 30.000"))

    preciofinal=precio*1.19

    if preciofinal>20000:
         preciofinal-=10000
         print("precio alto")
    else:
         preciofinal-=5000
         print("precio normal")
    
    print("el precio final es de $ "+str(preciofinal))

    seguir=input("desea ingresar otro precio (S/N)").lower()
    while seguir!="s" and seguir!="n":
        seguir=input("desea ingresar otro precio (S/N)").lower()

print("fin del programa ")  


    