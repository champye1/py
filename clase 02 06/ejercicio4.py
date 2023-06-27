'''
Ingresar números según un cálculo matemático variable.
Estos ingresos se harán midiendo el tiempo, hasta cumplir 4 aciertos o hasta no acertar un número.
'''

from time import time
from random import randint
acierto=0
num=randint(1,9)
inicio = time()

while True:
    num1=int(input('Ingrese el doble de '+str(num)+', más 6='))
    num2=num*2+6
    num=num2+round(time()-inicio) #esta suma crece según el tiempo
    if num2!= num1:
        print('Te equivocaste')
        break
    else:
        acierto=acierto+1
    print(acierto,'acierto(s)')
    if acierto==4:
            fin = time()
            print('Lo lograste en',round(fin-inicio),'seg')
            break
