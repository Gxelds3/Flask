#definir una variable
a = 1

#definir una funcion
def find_n(a):
    #aqui definimos el metodo por buenas practicas debe de llevar esto cada funcion
    #seria el nombre de la funcion nombre y fecha realizada, parametros que seria
    #la variable a de tipo entero, return seria un String una cadena
    """
    find_n | Gael Flores | 2026-09-03
    Modified:
        2026-09-03 | inicial version | Gael Flores

    Params:
        a int

    Returns:
        String
    """

    #if(a):
    #imprime la variable que imprimiria "1"
    print(a)

    #retorna la variable que imprimiria "1"
    return str(a)

    #imprime el la variable "a" pero con el proceso de la Funcion y imprime "1"
print(find_n(a))


#arreglo de listas
Lista_a = ['A','B','C','D','E',]

#de esta cadena de letras de la A a la E. Aqui esta todo junto
abc = 'ABCDE'

#imprime de la lista_a la posicion 0 que seria la letra "A"
print(Lista_a[0])

#aqui de esta cadena selcionas la posicion 2 y quitas la ultima y imprime CD osea quita "ABE"
print(abc[2:-1])
