


# print(nums)
# Imprime en consola el contenido de la lista 'nums'.

# colors.append('violeta')
# Añade el elemento 'violeta' al final de la lista.

# colors.extend(['Fiusha','Naranaja'])
# Añade múltiples elementos a la vez al final de la lista.

# colors.insert(0, 'Violeta')
# Inserta el elemento 'Violeta' en una posición específica (en este caso, en el índice 0).

# colors.clear()
# Elimina absolutamente todos los elementos de la lista, dejándola vacía.

# colors.append('violeta')
# Vuelve a añadir 'violeta' al final de la lista.

# print(colors.pop())
# Elimina y devuelve el último elemento de la lista (y luego lo imprime).

# colors.sort(reverse=True)
# Ordena la lista alfabéticamente de forma descendente (de la Z a la A).

# colors.sort(reverse=False)
# Ordena la lista alfabéticamente de forma ascendente (de la A a la Z).

# colors.reverse()
# Invierte el orden actual de los elementos de la lista (solo le da la vuelta al orden actual).

# color_1 = colors.copy()
# Crea una copia independiente de la lista 'colors' y la guarda en 'color_1'.

# print(color_1)
# Imprime la nueva lista copiada.

# print(colors)
# Imprime la lista original 'colors'.

#arreglo de numeros del uno al diez pero escrito
nums = ['Uno','Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho','Nueve','Diez']

#arreglo de colores son diez en total diferentes
colors = ['Azul','Rojo','Amarillo','Blanco','Negro','Verde','Cafe','Morado','Rosa','Gris']

#este fue el de referencia lo tome para hacer la actividad si no se me olvida o pierde
#sirve para imprimir todos los valores en orden el primer numero con el primer color.
"""for num in nums:
    output = f"[{num}, {colors[nums.index(num)]}]"
    print(output)"""

#esta es la varable donde vamos a pasar el arreglo
new_lista = []
for num in nums:
    output = f"[{num}, {colors[nums.index(num)]}]"
    #los valores imprimidos los pasas a la varable de "new_lista" y los empuja con el "append"
    new_lista.append(output)
    #volteas la lista 
    new_lista.reverse()
    #imprimes la nueva lista
print(new_lista)


#este print imprime el primer elemento de nums y colors
#print([nums[0], colors[0]])
