try:
    matricula=int(input("ingrese cantidad de matriculas = "))
    meta=int(input("ingresa meta de matriculas = "))
    cumplimiento=(matricula/meta)*100
    print("cumpliminetos = ",round(cumplimiento,2),'%')
    print(8*'*'+'operacion finalizada '+8*'*' )
except:
    print("error se esta dividiendo por 0")
print(8*'*'+'operacion finalizada '+8*'*' )