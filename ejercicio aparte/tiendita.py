'''Una tienda ofrece los siguientes descuentos por el monto de compra de los clientes, mientras responda s para seguir: 
Leer un monto inicial de compra (validar como mayor a 0).
Calcular el monto final de la compra, de la sgte. manera: 

-Si el monto inicial es menor a $100.000, descuento de 0%
-Si el monto inicial es mayor o igual a $100.000 y menor a $500.000, descuento de 5%.
-Si el monto inicial es mayor o igual a $500.000, descuento de 20%. 

Finalmente, mostrar la suma de los montos finales, que ingresa a la tienda.  '''
montofinal=0
totalcompra=0
seguir="s"


while seguir=="s":
    montoinicial=int(input("ingresa una cantidad inicial validad para la compra = "))
    while montoinicial<=0:
        montoinicial=int(input("error, ingresa el monto inicial de compra: "))


        if montoinicial<100000:
         montofinal=montoinicial
        elif montoinicial>=100000 and montoinicial<500000:
         montofinal=montoinicial*0.95
        else:
             montofinal=montoinicial*0.8
        totalcompra+=montofinal

        
    seguir=input("desea ingresar otro seguro (S/N)")
    while seguir!="s" and seguir!="n":
        seguir=input("ingresa si quieres seguir con (S/N)").lower()

print("el total a pagar es = ",totalcompra)
