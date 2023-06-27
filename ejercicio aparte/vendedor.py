'''
Una empresa de seguros desea calcular cuánto dinero obtendrá un vendedor por concepto de las ventas que realiza en el mes.
Leer el sueldo base de un vendedor (validar como mayor a 0). 
Mientras responda s para seguir: 

Leer un tipo de seguro que vende (validar el tipo de seguro permitiendo sólo las letras a, b o c)
La comisión se calcula de la siguiente manera: 

Si el tipo de seguro que vende es a, la comisión será 4.3% del sueldo base.
Si el tipo de seguro que vende es b, la comisión será 5.2% del sueldo base.
Si el tipo de seguro que vende es c, la comisión será 8.7% del sueldo base. 

Finalmente, mostrar el total que recibirá en el mes tomando en cuenta su sueldo base más sus comisiones. '''
seguir="s"
comision=0
sueldototal=0
sueldo=int(input("ingresar sueldo ="))
while sueldo<0:
    sueldo=int(input("error, ingrese sueldo mayor a 0 = "))
while seguir=="s":
    seguro=input("ingresa el tipo de seguro a/b/c = ")
    while seguro!="a" and seguro!="b" and seguro!="c":
        seguro=input("error ingresa seguro a/b/c =")
    if seguro=="a":
        comision+=sueldo*0.043
        sueldototal=comision+sueldo
    elif seguro=="b":
         comision+=sueldo*0.052
         sueldototal=comision+sueldo
    else:
         comision+=sueldo*0.087
         sueldototal=comision+sueldo
    seguir=input("desea ingresar otro seguro (S/N)")
    while seguir!="s" and seguir!="n":
        seguir=input("ingresa si quieres seguir con (S/N)").lower()
print("su sueldo es de =",sueldototal)

             
