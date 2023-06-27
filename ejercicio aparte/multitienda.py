'''
En una multitienda nacional se desea calcular el total en ventas de este mes de los artículos, en cada sucursal, para esto se debe construir un algoritmo que realice lo siguiente:

Ingresar la cantidad de sucursales a considerar (validar entre 2 y 4).

Para cada una de las sucursales, pedir la cantidad de artículos a considerar (validar entre 2 y 5).

Para cada artículo, pedir la cantidad vendida y el precio (validarlos mayor a 0), y multiplicar estos para tener el total de la venta.

Ir sumando el total de venta de cada artículo de todas las sucursales.

Al final se debe mostrar el total de ventas final de todos los artículos.

(Pista: se debe anidar un for dentro de otro. El for de afuera para la cantidad de sucursales y el for de adentro para la cantidad de artículos.) 

'''

j=0
i=0
totalventas=0

sucursal=int(input("ingresa la cantidad de sucursales a conciderar (entre 2 y 4 )"))
while sucursal<2 or sucursal>4:
    sucursal=int(input("error, ingresa la cantidad de sucursales a conciderar (entre 2 y 4 )"))

for i in range(sucursal):
    articulo=int(input("ingresa la cantidad de articulos a conciderar (ente 2 y 5): "))
    while articulo<2 or articulo>5:
        articulo=int(input("error, ingresa la cantidad de articulos a conciderar (ente 2 y 5): "))
        


    for j in range(articulo):
        cantidad=int(input("ingresa la cantidad vendida del articulo : "))
        while cantidad<=0:
            cantidad=int(input("error, ingrese una cantidad valida del articulo"))
        
        precio=int(input("ingresa el precio del articulo: "))
        while precio<=0:
            precio=int(input("ingresa el precio del articulo: "))


        totalventas+=cantidad *precio

print("el total de ventas es de $ "+str(totalventas))

            
