'''Leer el stock de los productos notebook, impresoras y smartphone (validar como mayor a 0). 
Mientras se responda s a seguir: 

Leer, como string, el código de producto (validar distinta vacío, distinto a comillas vacías) 

Leer un pedido de este producto (validar como mayor a 0) 

Si el pedido es menor o igual al stock de ese producto, rebajar el stock de ese producto, sino avisar que no hay stock suficiente de ese producto. 

Al finalizar, entregar el stock de cada producto. 
'''
seguir="s"

note=int(input("ingresar stock notebook = "))
while note<=0:
    note=int(input("ingresar stock notebook = "))

impresora=int(input("ingresar stock impresoras = "))
while impresora<=0:
    impresora=int(input("ingresar stock notebook = "))

celular=int(input("ingresa cantidad de stock de los celulares "))
while celular<=0:
    celular=int(input("ingresar stock notebook = "))

while seguir=="s":
    codigo=input("ingresar codigo del producto = ").lower()
    while codigo==""or codigo==" ":
        codigo=input("ingresar codigo del producto = ").lower()
    pedido=int(input(" ingresar el pedido de este producto = "))
    if codigo=="notebook":
        if pedido<=note:
            note-=pedido
        else:
            print("no hay stock suficiente de notebook")
    if codigo=="impresora":
        if pedido<=impresora:
            impresora-=pedido
        else:
            print("no hay stock suficiente de impresoras")
    if codigo=="celular":
        if pedido<=celular:
            celular-=pedido
        else:
            print("no hay stock suficiente de celular")
    else:
        print("codigo de producto invalido (ingrese :notebook/impresora/celular)") 

    seguir=input("desea continuar comprando (s/n)").lower()
    while seguir!="s" and seguir!="n":
        seguir=input("error, ingresa (s/n)").lower() 

print("el stock de notebook es de ="+str(note))
print("el stock de notebook es de ="+str(impresora))
print("el stock de notebook es de ="+str(celular))

