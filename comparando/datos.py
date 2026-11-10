
""" Comparo 'datos' usando la libreria visor-vari.\n
    (english translation) \n
    I compare 'data' using the visor-vari library.
    
"""


#################################
#   Importaciones.
"==============================="

en_prueba= False
if en_prueba == False:
    
    from visor_vari._procesos.code import ejecuto
        
def preconfg_primero(bloque_a, selda_a, bloque_b, selda_b):
    """Señale la primera y segunda selda, de entrada ('selda_a' y 'selda_b' respectivamente)\n
    Recuerde que:\n
    - fila (0, 1, 2) "es el bloque (movimiento vertical que señala elementos 
    ordenados horizontalmente)"\n
    - columna (0, 1, 2) "es la selda (movimiento horizontal que señala
    elementos ordenados verticalmente)"\n
    (english translation)\n
    Point out the first and second cells, at the entrance ('selda_a' and 'selda_b' respectively).\n
    Remember that:\n
    - row (0, 1, 2) is the block (vertical movement that selects horizontally ordered elements)\n
    - column (0, 1, 2) is the cell (horizontal movement that selects vertically ordered elements)\n
    """
    ejecuto.preconfg_primero(bloque_a, selda_a, bloque_b, selda_b)

def porvalor(back= True, bloque= None, selda= None):
    """Devuelve el valor en 'selda_b', si es diferente a 'selda_a'.\n
    Recuerde que:\n
    - back= 'True' (le regresa una lista)\n
    - back= 'False' (aloja el resultado, en la selda 
    de salida escogida)\n
    'Bloque' y 'selda' aquí son la salida, en la que se guardaran los datos \n
    (excepto cuando 'back'= True)\n
    (english translation)\n
    Returns the value in 'selda_b' if it's different from 'selda_a'.\n
    Remember that:\n
    - back = 'True' (returns a list)\n
    - back = 'False' (stores the result in the chosen output cell)\n
    'Block' and 'selda' here are the output cells where the data will be saved
    (except when 'back' = True)\n
    """
    return ejecuto.porvalor(back, bloque, selda)

def porboolean(back= True, bloque= None, selda= None):
    """Devuelve 'True' si 'selda_a' y 'selda_b' son diferentes.
    si son iguales debuelve 'False'.\n
    Recuerde que:\n
    - back= 'True' (le regresa una lista)\n
    - back= 'False' (aloja el resultado, en la selda 
    de salida escogida)\n
    'Bloque' y 'selda' aquí son la salida, en la que se guardaran los datos \n
    (excepto cuando 'back'= True)\n
    (english translation)\n
    Returns 'True' if 'selda_a' and 'selda_b' are different.\n
    If they are equal, it returns 'False'.\n
    Remember that:\n
    - back = 'True' (returns a list)\n
    - back = 'False' (stores the result in the chosen output cell)\n
    'Block' and 'selda' here are the output cells where the data will be saved
    (except when 'back' = True)\n
    """
    return ejecuto.porboolean(back, bloque, selda)

def valorsuperior(back= True, bloque= None, selda= None):
    """Devuelve los valores de 'selda_b' cuando son superiores a 'selda_a'.\n
    Recuerde que:\n
    - back= 'True' (le regresa una lista)\n
    - back= 'False' (aloja el resultado, en la selda 
    de salida escogida)\n
    'Bloque' y 'selda' aquí son la salida, en la que se guardaran los datos \n
    (excepto cuando 'back'= True)\n
    (english translation)\n
    Returns the values of 'selda_b' when they are greater than 'selda_a'.\n
    Remember that:\n
    - back = 'True' (returns a list)\n
    - back = 'False' (stores the result in the chosen output cell)\n
    'Block' and 'selda' here are the output cells where the data will be saved
    (except when 'back' = True)\n
    """
    return ejecuto.valorsuperior(back, bloque, selda)

def booleansuperior(back= True, bloque= None, selda= None):
    """Devuelve 'True' si 'selda_b' es superior a
    'selda_a'. De lo contrario debuelve 'False'.\n
    Recuerde que:\n
    - back= 'True' (le regresa una lista)\n
    - back= 'False' (aloja el resultado, en la selda 
    de salida escogida)\n
    'Bloque' y 'selda' aquí son la salida, en la que se guardaran los datos \n
    (excepto cuando 'back'= True)\n
    (english translation)\n
    Returns 'True' if 'selda_b' is greater than 'selda_a'.\n
    Otherwise, returns 'False'.\n
    Remember that:\n
    - back = 'True' (returns a list)\n
    - back = 'False' (stores the result in the chosen output cell)\n
    'Block' and 'selda' here are the output cells where the data will be saved
    (except when 'back' = True)\n
    """
    return ejecuto.booleansuperior(back, bloque, selda)

def valorinferior(back= True, bloque= None, selda= None):
    """Devuelve los valores de 'selda_b' cuando son 
    inferiores a 'selda_a'.\n
    Recuerde que:\n
    - back= 'True' (le regresa una lista)\n
    - back= 'False' (aloja el resultado, en la selda 
    de salida escogida)\n
    'Bloque' y 'selda' aquí son la salida, en la que se guardaran los datos \n
    (excepto cuando 'back'= True)\n
    (english translation)\n
    Returns the values of 'selda_b' when they are less than 'selda_a'.\n
    Remember that:\n
    - back = 'True' (returns a list)\n
    - back = 'False' (stores the result in the chosen output cell)\n
    'Block' and 'selda' here are the output cells where the data will be saved
    (except when 'back' = True)\n
    """
    return ejecuto.valorinferior(back, bloque, selda)

def booleaninferior(back= True, bloque= None, selda= None):
    """Devuelve 'True' si 'selda_b' es inferior a
    'selda_a'. De lo contrario debuelve 'False'.\n
    Recuerde que:\n
    - back= 'True' (le regresa una lista)\n
    - back= 'False' (aloja el resultado, en la selda 
    de salida escogida)\n
    'Bloque' y 'selda' aquí son la salida, en la que se guardaran los datos \n
    (excepto cuando 'back'= True)\n
    (english translation)\n
    Returns 'True' if 'selda_b' is less than 'selda_a'.\n
    Otherwise, returns 'False'.\n
    Remember that:\n
    - back = 'True' (returns a list)\n
    - back = 'False' (stores the result in the chosen output cell)\n
    'Block' and 'selda' here are the output cells where the data will be saved
    (except when 'back' = True)\n
    """
    return ejecuto.booleaninferior(back, bloque, selda)

def confg_piso(sign= 0, continuo= True):
    """Establece un signo para las seldas que siguen siendo las mismas.\n
    (english translation)\n
    Sets a sign for cells that are the same.\n
    """
    ejecuto.confg_piso(sign, continuo)
    
