#lso string o cadenas nos han permitido escribir y leer textos

'''
con la funcion len es posible obtener el largo de un string
'''


'''
codigo=input("ingrese codigo (largo 8) ="  )
while len(codigo)!=8:
    codigo=input("error ingrese codigo con largo 8 =")
print("el codigo eingresado es = ", codigo)
'''


'''
nombre=input("ingrese su equipo de futbol !="+"  ")

cant=int(input("cuantas veces lo desa mostrar ? ="))

print(nombre * cant)


'''

'''

escribir en pantalla un texto con comilla o cremillas
es es posible hacer esto de diferentes maneras
'''

'''
print("escribiendo 'python' entre cremillas")
print('escribiendo "python" entre comillas')
print("escribiendo \'python\' entre comillas")
print("escribiendo \"python\" entre comillas")
print('escribiendo \'python\' entre comillas')
print('escribiendo \"python\" entre comillas')
'''

#rebanadas(slices de cadenas de caracteres 

'''
a veces es necesario extraer partes de una cadena,o sea , crear una subcadena o substring. para hacer esto se aplican rebanadas

para crear rebanadas se usa la notacion [inicio:fin:paso]'''


'''
texto="programador en python"
recibe=texto[0:8]
print(recibe)
'''

'''
texto="programando en python"
recibe=texto[2:14:2] elprograma leera desde la tercera letra hasta la letra 13 y cada 2 pasos
print(recibe)


'''


'''

texto="programando en python"
recibe=texto[:11]
print(recibe)

'''

'''
texto="programando en python"
recibe=texto[7:]
print(recibe)
'''

'''
texto="programando en python"
recibe=texto[::-1]
print(recibe)
'''

'''
texto=input("ingrese texto = ").lower()
alrevez=texto[::-1]
print(alrevez)
if texto==alrevez:
    print("es palindromo")
'''


'''
correo=input("ingrese correo=") 

if correo.count("@")==1:#metodo una funcion que se aplica a un objeto
    print("bien con @")
else:
    print("tiene mas @ o no tiene @")
if correo.count(".")>=1:
    print("bien con el .")
else:
    print("error en .")

'''
'''
#buscar un substring en el string, y entrega su pocicion fin

texto=input("ingrese un texto = ") # por ejemplo, escribir programa
busca=input("que busca? = ")#por ejemplo, escribir a 
encuentra=texto.rfind(busca)
if encuentra>=0:
    print("se encontro = ",encuentra)
else:
    print("no hay palabra con la letra solicitada")

    #find busca de izquierda a derecha 
    #si se cambia por rfind busca de derecha a izquierda'''


'''
#strip, rstrip y lstrip

#elimina espacios del string.

texto1="   un ejemplo   "
inicio="->"
fin="<-"

print (inicio+texto1+fin)
texto2=texto1.strip()#remueve el espacio en ambos costados

print(inicio+texto2+fin)

texto3=texto1.rstrip() #remueve el espacio de la derecha

print(inicio+texto3+fin)

texto4=texto1.lstrip() #remueve el espacio de la izquierda

print(inicio+texto4+fin)

'''

'''
#replace

#remplaza un substrip del string

texto="utilisando pithon"
texto=texto.replace("s","z")

print(texto)
'''

texto=input("ingresar texto = ")

while True:
    if texto.find("ñ")>=0:
        texto=texto.replace("ñ","nh")
        print(texto)
    else:
        break
print("fin")