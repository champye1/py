#inacializar variable

totalhoras=0
i=0

obreros=int(input("ingresar cantidad obreros"))
while obreros<=0:
    obreros=int(input("ingresar cantidad obreros"))

while i<obreros:
    nombre=input("ingresa el nombre de obrero ")
    while nombre=="" or nombre==" ":
        nombre=input("error, ingresa el nombre de obrero ")
    horas=int(input("ingresa la cantidad de horas trabajadas"))
    while horas<=0:
        horas=int(input("ingresa la cantidad de horas trabajadas"))
    totalhoras+=horas
    i+=1
totalpagar=totalhoras*4500

print("el total a pagar es de $ ",totalpagar)
        
        
    