#ingresar estudiantes y aprobados

estudiantes=int(input("ingresa la cantidad de estudiantes = "))
aprobados=int(input("ingresa la cantidad de aprobados"))

#validar

while estudiantes <=0 :
    estudiantes=int(input("error, ingrese cantidad valia de estudiantes"))
while aprobados<0 or aprobados > estudiantes:
    aprobados=int(input("error ingrese cantidad validad de aprobados = "))

#calculo %

porcentaje=(aprobados/estudiantes)*100
if porcentaje > 80 :
    print("rendimiento normal")
else:
    print("rendimiento bajo")