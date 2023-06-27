try:
    matricula=int(input("ingrese cantidad de matriculas = "))
    meta=int(input("ingresa meta de matriculas = "))
    cumplimiento=(matricula/meta)*100
    print("cumpliminetos = ",round(cumplimiento,2),'%')
    print(8*'*'+'operacion finalizada '+8*'*' )
except ValueError: #error de numero
    print("error de numero")
except ZeroDivisionError: #error de numero 0
    print("error se esta dividiendo por cero")
except: #otros errores 
    print("otro error")
else:
    print("no hay errores")
print(8*'*'+'operacion finalizada '+8*'*' )