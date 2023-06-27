'''from random import *

intento=0
cantEstudiante=randint(1,30)
totalnota=0

for i in range(cantEstudiante):
    nota=float(uniform(1.0,7.0))
    print("nota del estudiante ",i+1,round(nota,2))
    totalnota+=1
promedionota=totalnota/nota
print("el promedio final es de = ",promedionota)
'''


from random import randint,uniform

sumaNotas=0
cantEstudiantes=randint(1,30)

for i in range(cantEstudiantes):
    nota=uniform(1,7)
    print("nota "+str(i+1)+" = ",round(nota,2))
    sumaNotas+=nota
promedionota=sumaNotas/cantEstudiantes
print("promedio de notas de los estudiantes",round(promedionota,2))

