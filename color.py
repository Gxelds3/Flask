#defifir la varable con nuestro nombre grupo y un color.
ident='Angel Gael Flores Ronces | 4 B | Blanco'
#Declarar una funcion y con el parametro "ident"
def encontra_Color(ident):
        #aqui definimos el metodo por buenas practicas debe de llevar esto cada funcion
    #seria el nombre de la funcion nombre y fecha realizada, parametros que seria
    #la variable a de tipo entero, return seria un String una cadena
    """
    find_n | Gael Flores | 2026-09-03
    Modified:
        2026-09-04 | inicial version | Gael Flores

    Params:
        ident int

    Returns:
        String
    """
    #returna la variable y quitandole los primeros 33 caracteres
    return(ident[33:])

#El print arroja de la funcion el valor retornado y imprime "Blanco"
print(encontra_Color(ident))
