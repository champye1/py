suma=0
cantidad = int(input('Ingrese la cantidad de cajas a ingresar='))

for caja in range(cantidad):
    codigo = input('Ingrese el codigo de la caja '+str(caja+1)+' (largo 6)=')
    while len(codigo) != 6:
        codigo = input('Error, el largo debe ser de 6 caracteres, ingrese nuevamente=')
    try:
        cantProd = int(codigo[2:4])
        suma+=cantProd
    except ValueError:
        print("error de numero")
        cantidad=cantidad-1
if cantidad<0:
    promedio = suma/cantidad
    print('Promedio=',promedio)