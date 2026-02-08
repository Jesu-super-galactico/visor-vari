
""" Este modulo configura las visualizaciones, segun la activcion
    de los refer_x. """
    
    
"==============================="
#   importaciones
################################

from visor_vari.mas_bajo_nivel.datos import verifico

"==============================="

def nueva_confg(lista_de_configuracion):
    "esta funcion se encarga de configurar las visualizaciones, segun la activacion de los refer_x."
    
    si= True
    
    for r in lista_de_configuracion:
        if r == 0:
            verifico.estado_refer_0= si
        elif r == 1:
            verifico.estado_refer_1= si
        elif r == 2:
            verifico.estado_refer_2= si
        elif r == 3:
            verifico.estado_refer_3= si
        elif r == 4:
            verifico.estado_refer_4= si
        elif r == 5:
            verifico.estado_refer_5= si
        elif r == 6:
            verifico.estado_refer_6= si
        elif r == 7:
            verifico.estado_refer_7= si
        elif r == 8:
            verifico.estado_refer_8= si
        elif r == 9:
            verifico.estado_refer_9= si
    
