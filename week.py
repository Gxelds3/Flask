
#Angel Gael Flores Ronces | 4 B | 2026-09-04

#Arreglo de la semana con 6 posiciones
week = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
#nueva varable
out = []
#hacer un for con la posicion con enumerete enumeras los dias
for i, day in enumerate(week):
    #aqui va arrepetir el codigo hasta llegar hasta cumplir esta condicion
    if day == 'Sabado' or day == 'Domingo':  
        #lo asignas a la nueva variable y empujas el otro valor
        out.append(i)
        #imprimes ya el resultado seria [5, 6]
print(out) 